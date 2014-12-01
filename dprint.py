"""
Who:    Claus Frein
Why:    Collection of small python-snippets
When:   20120131: Created
"""

DEBUG=True

########################################

def dprint(*args):
    """Debug-Print"""

    if DEBUG:
        message = " ".join([str(x) for x in args])
        print(message)

