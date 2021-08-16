def dict_get(mydict, list_keys, default=None):
    assert isinstance(mydict, dict)
    assert isinstance(list_keys, (list, tuple))
    num_keys = len(list_keys)
    if num_keys == 1:
        return mydict.get(list_keys[0], default)
    elif list_keys[0] not in mydict:
        return default
    else:
        return dict_get(mydict[list_keys[0]], list_keys[1:], default)


def dict_set(mydict, list_keys, value):
    assert isinstance(mydict, dict)
    assert isinstance(list_keys, (list, tuple))

    assert len(list_keys) > 0

    if len(list_keys) == 1:
        mydict[list_keys[0]] = value
        return

    dict_set(mydict.setdefault(list_keys[0], dict()), list_keys[1:], value)


def dict_has_keys(mydict, list_keys):
    """
        check if specified dict has nested keys defined by list_keys
    :param mydict:
    :param list_keys:
    :return: check if specified dict has nested keys like: mydict[list_keys[0]][list_keys[1]] ...
    """
    assert isinstance(list_keys, (list, tuple))

    if not isinstance(mydict, dict):
        return False

    if len(list_keys) == 1:
        return list_keys[0] in mydict

    if list_keys[0] in mydict:
        return dict_has_keys(mydict[list_keys[0]], list_keys[1:])
    else:
        return False
