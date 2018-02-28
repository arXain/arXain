import os
import ipfsapi
import json
from distutils.dir_util import copy_tree
from werkzeug.utils import secure_filename
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
        ALLOWED_EXTENSIONS = set(['txt','pdf'])
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def upload_paper(self, request):
        if request.method == 'POST':
            print(request.files)
            # check if the post request has the file part
            if 'paper' not in request.files:
                flash('No file part')
                file_present = False
            file = request.files['paper']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                file_present = False
            if file and self.allowed_file(file.filename):
                #make an upload dir if it doesn't exist
                folder = self.arxain_path+'/upload'
                if not os.path.exists(folder):
                        os.makedirs(folder)
                #delete files already in upload folder
                for the_file in os.listdir(folder):
                    file_path = os.path.join(folder, the_file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        print(e)
                #copy file to upload folder
                filename = secure_filename(file.filename)
                file.save(os.path.join(self.arxain_path, 'upload', filename))
                file_path = self.arxain_path+'/upload'
                print(file_path)
                file_present = True
        results = {}
        results['Success'] = file_present
        results['fileDirectory'] = file_path
        results['fileName'] = filename

        return results

    def submit_manuscript(self, author_id, paper_id, paper_directory):
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
            output['Succcess'] = False
            output['Message'] = "Author ID {:s} not initialized.".format(author_id)
            return output

        # TODO:
        # Find the necessary files in the directory

        # Check that a valid manuscript file has been provided (pdf only, <=4 pages)
        #manuscript_result = self.check_manuscript_file(pdf_location)

        # return the error message if the manuscript check failed
        #if not manuscript_result['Success']:
        #    return manuscript_result

        # Check metadata validity

        # return error message if the metadata check failed

        # look for other files and do something?
        # END TODO

        # check if directory already exists
        ipfs_paper_path = os.path.join(author_check['author_path'], 'manuscripts', \
         paper_id)
        directory_check = os.path.exists(ipfs_paper_path)

        # find version number if paper already submitted
        if directory_check :
            n_versions = len(next(os.walk(ipfs_paper_path))[1])
            version_number = n_versions + 1
            v_string = 'v{:d}'.format(version_number)

        # assign version to be 1
        else :
            v_string = 'v1'

        # create the directory
        version_path = os.path.join(ipfs_paper_path, v_string)

        os.makedirs(version_path)

        # copy contents of the supplied directory to the new directory
        copy_tree(paper_directory, version_path)

        # publish paper_id/v# to IPFS
        # *** NOTE *** current ipfs api is not allowing us to submit a recursive
        # large directory. More recent versions have this, but I haven't tried building
        # them from source to try out. This should be remedied in the future.
        try :
            reply = self.api.add(version_path, recursive=True)
        except :
            # If any error occurs just return a sign of failure
            output = {}
            output['Success'] = False
            output['Message'] = 'ipfs submission failed.'

            # need to delete the already made directories...

            return output

        direc_hash = reply[-1]
        # save hash data to local database?

        # success message along with hash and version #
        #re-publish ipns ?
        output = {}
        output['Success'] = True
        output['Version'] = v_string
        output['Hash'] = direc_hash['Hash']

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
            output['Succcess'] = False
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
            output = self.submit_manuscript(author_id, paper_id, revision_directory)

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
            output['Succcess'] = False
            output['Message'] = "Author ID {:s} not initialized.".format(author_id)
            return output

        # TODO:
        # Find the necessary files in the directory

        # Check that a valid comment has been provided

        # return the error message if the comment check failed

        # return error message if the metadata check failed

        # look for other files and do something?
        # END TODO

        # check if directory already exists
        ipfs_comm_path = os.path.join(author_check['author_path'], 'comments', \
         paper_id)
        directory_check = os.path.exists(ipfs_comm_path)

        # find version number if paper already submitted
        if directory_check :
            n_versions = len(next(os.walk(ipfs_comm_path))[1])
            version_number = n_versions + 1
            v_string = 'v{:d}'.format(version_number)

        # assign version to be 1
        else :
            v_string = 'v1'

        # create the directory
        version_path = os.path.join(ipfs_comm_path, v_string)

        os.makedirs(version_path)

        # copy contents of the supplied directory to the new directory
        copy_tree(comment_directory, version_path)

        # publish paper_id/v# to IPFS
        # *** NOTE *** current ipfs api is not allowing us to submit a recursive
        # large directory. More recent versions have this, but I haven't tried building
        # them from source to try out. This should be remedied in the future.
        try :
            reply = self.api.add(version_path, recursive=True)
        except :
            # If any error occurs just return a sign of failure
            output = {}
            output['Success'] = False
            output['Message'] = 'ipfs submission failed.'

            # need to delete the already made directories...

            return output

        direc_hash = reply[-1]
        # save hash data to local database?

        # success message along with hash and version #
        #re-publish ipns ?
        output = {}
        output['Success'] = True
        output['Version'] = v_string
        output['Hash'] = direc_hash['Hash']

        return output

    def check_author(self, author_id):
        """Check whether the author ID has been created in the local directory. """
        author_path = os.path.join(self.arxain_path, 'authors', author_id)
        result = os.path.exists(author_path)

        output = {}
        output['Success'] = result
        output['author_path'] = author_path
        return output

    def check_manuscript_file(self, pdf_location):
        """Verify that the files submitted for a manuscript are valid"""
        pass

    def check_meta_data_json(self, meta_data):
        pass

    def check_comment_files(self):
        """Verify that the files submitted for a comment are valid."""
        pass
