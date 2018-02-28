import subprocess
import os
import json

def add_recursive(file_path, recursive=True, final_hash=True):
    """Add a file, or directory of files to IPFS recursively.
    Hopefully this is a temporary workaround to the API issues.

        Input Parameters:
        ----------
        file_path : str
            A filepath to either a file or directory
        recursive : bool
            Controls if files in subdirectories are added or not
        pattern : str | list
            Single `*glob* <https://docs.python.org/3/library/glob.html>`_
            pattern or list of *glob* patterns and compiled regular expressions
            to match the names of the filepaths to keep
        trickle : bool
            Use trickle-dag format (optimized for streaming) when generating
            the dag; see `the FAQ <https://github.com/ipfs/faq/issues/218>` for
            more information (Default: ``False``)
        only_hash : bool
            Only chunk and hash, but do not write to disk (Default: ``False``)
        wrap_with_directory : bool
            Wrap files with a directory object to preserve their filename
            (Default: ``False``)
        chunker : str
            The chunking algorithm to use
        pin : bool
            Pin this object when adding (Default: ``True``)
        Returns
        -------
            str: the hash of the file or outermost directory added

        Adapted from https://github.com/ipfs/py-ipfs-api/blob/master/ipfsapi/client.py
    """
    # Handle the optional inputs

    """
    Left these here in case we want to expand and build a wrapper around subprocess
    as opposed to the API call.
    opts = {
            "trickle": kwargs.pop("trickle", False),
            "only_hash": kwargs.pop("only_hash", False),
            "wrap_with_directory": kwargs.pop("wrap_with_directory", False),
            "pin": kwargs.pop("pin", True)
            }
    if "chunker" in kwargs:
            opts["chunker"] = kwargs.pop("chunker")

    kwargs.setdefault("opts", opts)
    """

    # Build the command list
    command = ["ipfs", 'add', file_path]

    if recursive :
        command.append('-r')

    if final_hash :
        command.append('-Q')

    print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE)

    output = result.stdout.decode('utf-8')
    return output
