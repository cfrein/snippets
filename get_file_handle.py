"""
Who:    Claus Frein
Why:    Collection of small python-snippets
When:   20120131: Created
"""

import os

def get_file_handle(filename, path=None, mode="r"):
    """open a file

    default to read-mode, raises an error if file not found
    """

    if path is not None:
        filename = os.path.join(path, filename)
    try:
        filehandle = open(filename, mode)
    except IOError as myerror:
        (errno, strerror) = myerror.args
        print("I/O error({0}): {1}".format(errno, strerror))
        raise
    return filehandle

