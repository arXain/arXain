from pyXain import ipfscmd
import os

def test_add_recursive():
    """ipfscmd.add_recursive"""
    # Get the test pdf in the folder
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(curr_dir, 'test-paper')
    output = ipfscmd.add_recursive(test_dir, recursive=True, final_hash=True)
