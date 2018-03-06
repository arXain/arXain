from pyXain import pyXain
import os
import json
import shutil
from glob import glob


def tearDown():
    """ Remove the test author at the end"""

    print('removing test directories in arXain-data...')
    pyx = pyXain()
    test_dir = os.path.join(pyx.arxain_path, 'authors', 'test_author')
    shutil.rmtree(test_dir)

def test_init():
    """create pyXain object"""
    # Test the class set up
    pyx = pyXain()
    pass

def test_init_arxain():
    """init_arxain"""
    # Test the initializtion of the directory structure
    pyx = pyXain()
    results = pyx.init_arxain()

    assert(results['Success'] == True)

    #try again
    results = pyx.init_arxain()
    assert(results['Success'] == True)

def test_init_author():
    """init_author"""
    # Test creating an author
    pyx = pyXain()
    result = pyx.init_author('test_author')
    print(result)
    assert(result['Success'] == True)

    # try again to re-init
    result2 = pyx.init_author('test_author')

    assert(result['peerID'] == result2['peerID'])

    #try again
    results = pyx.init_author('test_author')
    assert(results['Success'] == True)

def test_submit_manuscript():
    """submit_manuscript"""
    pyx = pyXain()

    # Get the test pdf in the folder
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    result = pyx.submit_manuscript('test_author', 'test_paper', os.path.join(curr_dir, 'test-paper'))
    print(result)
    assert(result['Success'] == True)

    # submit with wrong author
    result = pyx.submit_manuscript('not_an_initiallized_author', 'test_paper', os.path.join(curr_dir, 'test-paper'))
    print(result)
    assert(result['Success'] == False)

    # submit an empty directory
    result = pyx.submit_manuscript('test_author', 'test_paper', os.path.join(curr_dir, 'test-empty'))
    assert(result['Success'] == False)

def test_submit_revision():
    """submit_revision"""
    pyx = pyXain()

    # Get the test pdf in the folder
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    result = pyx.submit_revision('test_author', 'test_paper', os.path.join(curr_dir, 'test-paper-rev'))
    print(result)
    assert(result['Success'] == True)

    # submit with wrong author
    result = pyx.submit_revision('not_an_initiallized_author', 'test_paper', os.path.join(curr_dir, 'test-paper-rev'))

    assert(result['Success'] == False)

    # submit a non intialized paper
    result = pyx.submit_revision('test_author', 'NotAPaper', os.path.join(curr_dir, 'test-paper-rev'))

    assert(result['Success'] == False)

    # submit an empty directory
    result = pyx.submit_revision('test_author', 'test_paper', os.path.join(curr_dir, 'test-empty'))
    assert(result['Success'] == False)

    # submit a redundant paper
    result = pyx.submit_revision('test_author', 'test_paper', os.path.join(curr_dir, 'test-paper'))
    print(result)
    assert(result['Success'] == False)

def test_submit_comment():
    """submit_comment"""
    pyx = pyXain()

    # Get the test pdf in the folder
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    result = pyx.submit_comment('test_author', 'test_paper', os.path.join(curr_dir, 'test-comment'))
    print(result)
    assert(result['Success'] == True)

    # submit with wrong author
    result = pyx.submit_comment('not_an_initiallized_author', 'test_paper', os.path.join(curr_dir, 'test-comment'))

    assert(result['Success'] == False)

    # submit an empty directory_check# submit an empty directory
    result = pyx.submit_comment('test_author', 'test_paper', os.path.join(curr_dir, 'test-empty'))
    assert(result['Success'] == False)

"""
Still not working...
def test_check_author_valid():
    pyx = pyXain()

    # Check a valid author
    result_valid = pyx.check_author('test_author')

    assert(result_valid['Success'] == True)

    # Check an invalid author
    result_false = pyx.check_author('NotAnAuthor!')
    # check_author should return false when an invalid author is sent

    assert(result_false['Success'] == False)
"""
def test_get_extension():
    """get_extension"""
    pyx = pyXain()

    # check if the pdf is found in the test-paper directory
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    file_names = pyx.get_extension('pdf', os.path.join(curr_dir, 'test-paper'))

    base_name = [os.path.basename(x) for x in file_names]
    assert(base_name[0] == 'test_paper.pdf')

def test_allowed_file():
    """allowed_file"""
    pyx = pyXain()

    approved_names = ['test.txt', 'test.pdf', 'test.json']

    for file_name in approved_names :
        assert(pyx.allowed_file(file_name) == True)

    not_approved_names = ['test.doc', 'test.docx', 'test.rtf', 'test.js', 'test.html']
    for file_name in not_approved_names :
        assert(pyx.allowed_file(file_name) == False)

def test_hash_files():
    """hash_files"""

    # these hashes have to line up with the files posted
    actual_hashes = [b'h\xec\t\x068\xc8\xe1\xffj\xb3k\xba9\xabj\x1bTG?\x0b\xa1\x1f\x00\x8d7\xa6>\xb0Y\xb3(\x90P\x12P8pfn\x83p\xad\x02\x1d]m$\xb2!\xc9\xec/\xaf\xceOY\x98\x89\xdf\xf4\xe5\xdb\xc3\x8c', \
     b'\xcdbf\xbc\x01\xa6\x8d]1\xc3\x14BH\xc5\xfd\x8a\x08\x85\x14B[\x0f\x9c\x7f\x80A/9X\xb0\x07!\x89\xb5\xd8\x18+m\x80\xb5\x06nS4\xe5q\xc2O\xe4\x04E)P\xaf\xbf\xe8\xd2<\xe9\x93\x16\xbe\xfd\x06', \
     b"\xb9F~)3\x86\x86\x14\x96\xb9DI\x1c_\xe5\xaeq\xdaM\xbf\xce0\xeb\xf7\x96\x80\xdb\xb1_Dc\xd4u5\x88q\x9f8\x0f\n\xd3\xb6\x0f\x1c\x8a\x84\x8c\xd6\x9a \xcfr\x92\x0c'X\xab\xbez\xfa\xaf\x9d\xdb<"]
    pyx = pyXain()

    # Get the current directory and go intot he conflict-free (all unique) directory
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    conflict_free = os.path.join(curr_dir, 'test-hashes', 'conflict-free')

    # Get the full file paths, as a sorted list and hash them
    conf_free_files = glob(os.path.join(conflict_free, '*'))
    conf_free_files.sort()
    hash_list = pyx.hash_files(conf_free_files)

    # compare the calculated hashes to our standard
    for calc, actual in zip(hash_list, actual_hashes) :
        print('calc: ', calc)
        print('actual: ', actual)
        assert(calc == actual)

def test_verify_unique_revision():
    """verify_unique_revision"""

    pyx = pyXain()

    # Get the current directory and go intot he conflict-free (all unique) directory
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    conflict_free = os.path.join(curr_dir, 'test-hashes', 'conflict-free')

    # Get the full file paths as a list and hash them
    conf_free_files = glob(os.path.join(conflict_free, '*'))
    hash_list = pyx.hash_files(conf_free_files)

    # convert to format for using verify_unique_revision
    prev_hashes = {'v1' : hash_list[0], 'v2' : hash_list[1]}
    current_hash = hash_list[2]
    result = pyx.verify_unique_revision(prev_hashes, current_hash)

    assert(result['Success'] == True and len(result['overlaps']) == 0)

    # Check the conflicted directory
    conflict_filled = os.path.join(curr_dir, 'test-hashes', 'conflict-filled')

    # Get the full file paths as a list and hash them
    conf_filled_files = glob(os.path.join(conflict_filled, '*'))
    hash_list = pyx.hash_files(conf_filled_files)

    # convert to format for using verify_unique_revision
    prev_hashes = {'v1' : hash_list[0], 'v2' : hash_list[1]}
    current_hash = hash_list[2]
    result = pyx.verify_unique_revision(prev_hashes, current_hash)

    assert(result['Success'] == False and len(result['overlaps']) == 2)
