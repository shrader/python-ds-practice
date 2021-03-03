def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for small_list in lst:
        if not isinstance(small_list, list):
            return False

    return True