import os
import ipfsapi
import json
from distutils.dir_util import copy_tree
from glob import glob
import hashlib
from . import ipfscmd


#import PyPDF2 # for pdf file parsing in the future

class pyXain(object):
    """A means for interfacing with the arXain directory structure, hosted on
    IPFS, through Python.

    Attributes:
        api: the ipfsapi object through which we communicate with a local IPFS client
        arxain_dir: the outer arxain directory. Can be moved from the default ~/.arXain-data with config.json
        pin_list_dir: the directory of pinned hashes
        arxain_path: the full path for easily accessing directories
    """

    def __init__(self, config_loc="default"):
        """Return an ipfs object with the initial parameters defined by the config
        file @ config_loc. See config.json in the pyXain directory for config file
        format.

        Inputs:
            config_loc: the full file path to a config files
        """

        if config_loc is "default" :
            mydir = os.path.dirname(os.path.abspath(__file__))
            config_loc =os.path.join(mydir, 'config.json')

        with open(config_loc, 'r') as f:
            config = json.loads(f.read())

        self.api = ipfsapi.connect(config['ipfs_address'], config['ipfs_api_port'])
        self.arxain_dir = config['arxain_dir']
        output = self.init_arxain()
        self.arxain_path = output['Path']

    def init_arxain(self):
        """Initialize arXain locally at the chosen path. This sets up the broad
        directory structure and database files required to run successfully. The
        default is a hidden directory created in the users home directory at
        ~/.arXain-data.

        Inputs:
            self: the pyXain object

        Outputs:
            arxain_path: the full path to arxain
        """

        if self.arxain_dir[0] is "~" :
            user_home = os.path.expanduser("~")
        else :
            user_home = self.arxain_dir

        arxain_path = os.path.join(user_home, self.arxain_dir[1:])
        directory_check = os.path.exists(arxain_path)

        # Create the directory if it doesn't exist
        if not directory_check :
            print('Creating directory at {}'.format(arxain_path))
            os.makedirs(arxain_path)
            os.makedirs(os.path.join(arxain_path, "authors"))

            pin_directory = os.path.join(arxain_path, "pin_list")
            os.makedirs(os.path.join(arxain_path, "pin_list"))

            with open(os.path.join(pin_directory, 'pin_list.json'), 'w+') as f:
                direc = {}
                direc['paperID'] = {}

        output = {}
        output['Success'] = True
        output['Path'] = arxain_path
        return output

    def init_author(self, author_id):
        """ Function for initializing an author in the local arXain repository
        that will be used to host files on IPFS. Requires the home directory and
        the ether address of the author to be supplied in that order.

        Inputs:
            author_id: the unique author identifier (ethereum wallet address)

        Outputs:
            results['successFlag'] = key_present:  whether the program ran to completion
            results['peerID'] = peer_id: the public peer ID of this particular author (/ipns/<peer_id>)
            results['authorID'] = author_id: the author_id passed
            results['localDirectory'] = author_path: the local path to the newly created repository
        """

        # Create the author's repository if not made
        result = self.check_author(author_id)
        print(result)

        if not result['Success'] :
            author_path = os.path.join(self.arxain_path, 'authors', author_id)
            os.makedirs(author_path)

            # Make sub directories
            manuscript_path = os.path.join(author_path, 'manuscripts')
            comment_path = os.path.join(author_path, 'comments')

            os.makedirs(manuscript_path)
            os.makedirs(comment_path)

        else :
            author_path = result['author_path']
            print(author_path + "/ already exists")

        # Assuming IPFS is running, query for the key list to see if we need to set up
        # a key for this author.
        output = self.api.key_list()

        key_present = False
        for key in output['Keys']:

            if key['Name'] in author_id :
                key_present = True
                key_name = key['Name']
                peer_id = key['Id']
                break

        # Create the key if not present
        if not key_present :
            output = self.api.key_gen(key_name=author_id, type='rsa', size=2048)

            if output['Name'] == author_id :
                print("Successfully initialized ipfs key with {:s}".format(output['Name']))
                peer_id = output['Id']
                key_present = True
        else :
            print("Key {:s} already made with hash {:s}".format(key_name, peer_id))

        results = {}
        results['Success'] = key_present
        results['peerID'] = peer_id
        results['authorID'] = author_id
        results['localDirectory'] = author_path

        return results

    def allowed_file(self, filename):
        ALLOWED_EXTENSIONS = set(['txt','pdf','json'])
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def submit_manuscript(self, author_id, paper_id, paper_directory, init_sub=True):
        """ Publish a manuscript to IPFS that has already had a contract address created
        on the block chain. The author ID, paper ID (contract hash) and the local
        directory containing all of the files for upload must be passed. This
        function requires that the author has already been initialized.

        Inputs:
            author_id: what author is publishing the paper
            paper_id: the unique identifier of the paper
            paper_directory: the full local directory of the paper to be submitted

        Outputs:
            output['Success']: whether the file was added to IPFS successfully or not
            output['Version']: the version string ('v#')
            output['Hash']: the hash of the directory storing the paper
        """

        # Check whether the author has been initialized in the system.
        author_check = self.check_author(author_id)
        if not author_check['Success'] :
            output = {}
            output['Success'] = False
            output['Message'] = "Author ID {:s} not initialized.".format(author_id)
            return output

        # Find the pdf file in the directory
        pdf_file_name = self.get_extension('pdf', paper_directory)

        # Ensure only one pdf is being uploaded
        if len(pdf_file_name) is not 1:
            output = {}
            output['Success'] = False
            output['Message'] = "Only one PDF can be uploaded"
            return output

        # TODO:
        # Check whether the PDF is valid for upload. # pages, file size?
        # return the error message if the manuscript check failed

        # Force rename the file to the paper_id
        os.rename(pdf_file_name[0], os.path.join(paper_directory, paper_id+'.pdf'))

        # TODO:

        # Check metadata validity

        # return error message if the metadata check failed

        # look for other files and do something?
        # END TODO

        # check if directory already exists
        ipfs_paper_path = os.path.join(author_check['author_path'], 'manuscripts', \
         paper_id)
        dir_check = self.check_directory(ipfs_paper_path)

        # Return a failure if this isn't the first version
        if dir_check['versions'] != 0 and init_sub:
            results = {'Success': False, 'Message' : 'A version of this paper is already submitted.'}
            return results

        # check the uniqueness if this is a revision
        if not init_sub :
            # get the file paths
            prev_versions = []
            version_names = []
            for i in range(1, dir_check['versions'] + 1) :
                version_names.append('v{:d}'.format(i))
                prev_versions.append(os.path.join(ipfs_paper_path, \
                 version_names[-1], \
                 '{:s}.pdf'.format(paper_id)))

            print(prev_versions)

            # hash the previous n_versions
            hash_list = self.hash_files(prev_versions)
            current_file_name = [os.path.join(paper_directory,\
                '{:s}.pdf'.format(paper_id))]
            current_hash = self.hash_files(current_file_name)

            # Convert and check for uniqueness
            prev_hashes = dict(zip(version_names, hash_list))
            result = self.verify_unique_revision(prev_hashes, current_hash[0])

            # handle the case when there are confilicts
            if result['Success'] == False :
                result['Message'] = 'An exact copy of this paper has already been submitted.'
                return result

        v_string = 'v{:d}'.format(dir_check['versions'] + 1)

        # create the directory
        version_path = os.path.join(ipfs_paper_path, v_string)
        os.makedirs(version_path)

        # copy contents of the correct version path
        copy_tree(paper_directory, version_path)

        # submit the outer paper directory
        output = self.submit_content(ipfs_paper_path)

        if output['Success'] is False :
            return output

        #add the version string
        output['Version'] = v_string

        return output

    def submit_revision(self, author_id, paper_id, revision_directory):
        """Submit a revision of a manuscript to IPFS and return the hash. This
        checks whether the paper ID has already been submitted, and returns a
        failure message if it hasn't prompting the user to submit the paper.

        Inputs:
            author_id: what author is publishing the paper
            paper_id: the unique identifier of the paper
            revision_directory: the full local directory of the paper to be submitted

        Outputs:
            output['Success']: whether the file was added to IPFS successfully or not
            output['Version']: the version string ('v#')
            output['Hash']: the hash of the directory storing the paper

        """

        # Check whether the author has been initialized in the system.
        author_check = self.check_author(author_id)
        if not author_check['Success'] :
            output = {}
            output['Success'] = False
            output['Message'] = "Author ID {:s} not initialized.".format(author_id)
            return output

        # Check if paper has already been submitted
        ipfs_paper_path = os.path.join(author_check['author_path'], 'manuscripts', \
         paper_id)
        directory_check = os.path.exists(ipfs_paper_path)

        # Handle the error message, or submit the manuscript
        if not directory_check :
            output = {}
            output['Success'] = False
            output['Message'] = 'Initial paper directory not found. Can''t submit a revision'

        else :
            output = self.submit_manuscript(author_id, paper_id, revision_directory, init_sub=False)

        return output

    def submit_comment(self, author_id, paper_id, comment_directory):
        """Submit a comment on a particular paper.

        Inputs:
            author_id: what author is publishing the comment
            paper_id: the unique identifier of the paper under comment
            revision_directory: the full local directory of the comment to be published

        Outputs:
            output['Success']: whether the file was added to IPFS successfully or not
            output['version']: the version string ('v#')
            output['hash']: the hash of the directory storing the paper

        """
        # Check whether the author has been initialized in the system.
        author_check = self.check_author(author_id)
        if not author_check['Success'] :
            output = {}
            output['Success'] = False
            output['Message'] = "Author ID {:s} not initialized.".format(author_id)
            return output

        # Find the pdf file in the directory
        text_file_name = self.get_extension('txt', comment_directory)

        # Ensure only one pdf is being uploaded
        if len(text_file_name) is not 1:
            output = {}
            output['Success'] = False
            output['Message'] = "Only one .txt file can be uploaded"
            return output

        # TODO:
        # Check an author isn't commenting on their own paper

        # check if directory already exists
        ipfs_comm_path = os.path.join(author_check['author_path'], 'comments', \
         paper_id)
        dir_check = self.check_directory(ipfs_comm_path)

        # find version number if paper already submitted
        v_string = 'v{:d}'.format(dir_check['versions'] + 1)
        directory_check = os.path.exists(ipfs_comm_path)

        # create the directory
        version_path = os.path.join(ipfs_comm_path, v_string)

        os.makedirs(version_path)

        # copy contents of the supplied directory to the new directory
        copy_tree(comment_directory, version_path)

        # submit to IPFS and handle errors
        output = self.submit_content(ipfs_comm_path)

        if output['Success'] is False :
            return output

        #add the version string
        output['Version'] = v_string

        return output

    def submit_content(self, target_dir):
        """Submit content to IPFS with an author id, paper id, directory containing
        the information, as well as the type.

        Inputs:
            target_dir: the desired location of the content to be added to IPFS at

        Outputs:
            output['Success']: whether the directory was added to IPFS successfully or not
            output['Hash']: the hash of the directory storing the content

        """

        # publish paper_id/v# to IPFS
        # *** NOTE *** current ipfs api is not allowing us to submit a recursive
        # large directory. More recent versions have this, but I haven't tried building
        # them from source to try out. This should be remedied in the future.
        try :
            # go-ipfs api v0.4.7 has a bug that prevents recursively adding directories.
            # try this out with later go-ips versions, I think they should have fixed it
            # but it isn't released
            #reply = self.api.add(ipfs_paper_path, recursive=True)

            # Use the subprocess version to recursively add the whole paper directory
            dir_hash = ipfscmd.add_recursive(target_dir)
        except :
            # If any error occurs just return a sign of failure
            output = {}
            output['Success'] = False
            output['Message'] = 'ipfs submission failed.'

            # need to delete the already made directories...

            return output

        # save hash data to local database?

        # success flag
        #re-publish ipns ?
        output = {}
        output['Success'] = True
        output['Hash'] = dir_hash

        return output

    def check_author(self, author_id):
        """Check whether the author ID has been created in the local directory. """
        author_path = os.path.join(self.arxain_path, 'authors', author_id)
        result = os.path.exists(author_path)

        output = {}
        output['Success'] = result
        output['author_path'] = author_path

        return output

    def check_directory(self, directory):
        """ Checks whether a content directory exists, and returns the number
        versions already contained.

        Inputs:
            directory: the full path of the content directory_check

        Outputs:
            output['exists']: whether the directory exists (bool)
            output['versions']: the number of versions contained (int), returns
            0 if it doesn't exist
        """
        output = {}
        output['exists'] = os.path.exists(directory)

        # find version number if content already exists
        if output['exists'] :
            n_versions = len(next(os.walk(directory))[1])
            output['versions'] = n_versions

        else :
            output['versions'] = 0

        return output

    def get_extension(self, extension, directory):
        """ Check a directory for all files that have the extension ext

        Inputs:
            self: the pyXain class
            ext: the file extension being searched for
            directory: the full path of the directory

        Output:
            a list of full path file names that match the extension in the directory provided
        """
        return glob(os.path.join(directory,"*.{}".format(extension)))

    def hash_files(self, files):
        """ hash all of the documents specified by the file list according to
        sha3_512 and return their digests in a list.

        Inputs:
            files: a list of full file paths

        Outputs:
            hashes: a list of the digest of the hash for comparison
        """
        hash_list = []
        for file in files :
            with open(file, 'rb') as f:
                hash_list.append(hashlib.sha3_512(f.read()).digest())

        return hash_list

    def verify_unique_revision(self, prev_hashes, current_hash):
        """ Iterate over the dict with previous hashes and verify that none of
        them conflict with the current hash. Return a success flag and a brief
        message in the case of a failure.

        Inputs:
            prev_hashs: dict with keys of the versions ('v1', 'v2'...) and the sha3_512.digest() as the entry
            current_hash: the sha3_512.digest() of the version to be submitted

        Outputs:
            output['Success']: whether the hashes are unique
            output['overlaps']: a list of the conflicting versions
        """
        conflict_list = []
        conflict = []
        for version, v_hash in prev_hashes.items() :
            conflict.append(v_hash == current_hash)
            if conflict[-1] :
                conflict_list.append(version)

        output = {}
        output['Success'] = not any(conflict)
        output['overlaps'] = conflict_list

        return output

"""
Methods reserved for potential future implementation
    def check_manuscript_file(self, pdf_location):
        pass

    def check_meta_data_json(self, meta_data):
        pass

    def check_comment_files(self):
        pass
"""
