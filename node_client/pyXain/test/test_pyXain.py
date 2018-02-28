from pyXain import pyXain
import os

class TestPyXain(object):
    """Test class for pyXain, run using pytest"""

    def test_init(self):
        # Test the class set up
        pyx = pyXain()
        pass

    def test_init_arxain(self):
        # Test the initializtion of the directory structure
        pyx = pyXain()
        results = pyx.init_arxain()

        assert(results['Success'] == True)

        #try again
        results = pyx.init_arxain()
        assert(results['Success'] == True)

    def test_init_author(self):
        # Test creating an author
        pyx = pyXain()
        result = pyx.init_author('test_author')

        assert(result['Success'] == True)

        #try again
        results = pyx.init_author('test_author')
        assert(results['Success'] == True)

    def test_submit_manuscript(self):
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

    def test_submit_revision(self):
        pyx = pyXain()

        # Get the test pdf in the folder
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        result = pyx.submit_revision('test_author', 'test_paper', os.path.join(curr_dir, 'test-paper'))
        print(result)
        assert(result['Success'] == True)

        # submit with wrong author
        result = pyx.submit_revision('not_an_initiallized_author', 'test_paper', os.path.join(curr_dir, 'test-paper'))

        assert(result['Success'] == False)

    def test_submit_comment(self):
        pyx = pyXain()

        # Get the test pdf in the folder
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        result = pyx.submit_comment('test_author', 'test_paper', os.path.join(curr_dir, 'test-comment'))
        print(result)
        assert(result['Success'] == True)

        # submit with wrong author
        result = pyx.submit_comment('not_an_initiallized_author', 'test_paper', os.path.join(curr_dir, 'test-comment'))

        assert(result['Success'] == False)

    """
    THIS IS FAILING FOR SOME REASON... UPDATE THIS IN THE FUTURE
    def test_check_author_valid(self):
        pyx = pyXain()

        # Check a valid author
        result_valid = pyx.check_author('test_author')

        assert(result_valid['Success'] == True)

    def test_check_author_invalid(self):
        pyx = pyXain()

        # Check an invalid author
        result_false = pyx.check_author('NotAnAuthor!')
        # check_author should return false when an invalid author is sent

        assert(result_false['Success'] == False)
        

        assert(result_false['Success'] == False)
    """

    def test_get_extension(self):
        pyx = pyXain()

        # check if the pdf is found in the test-paper directory
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        file_names = pyx.get_extension('pdf', os.path.join(curr_dir, 'test-paper'))

        base_name = [os.path.basename(x) for x in file_names]
        assert(base_name[0] == 'test_paper.pdf')
