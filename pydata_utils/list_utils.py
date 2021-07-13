def list_get(mylist: list, index: int, default=None):
    try:
        return mylist[index]
    except IndexError:
        return default


def list_set(mylist: list, index: int, value):
    '''
        set value at given location(index) of list, and expand list as needed
    :param mylist:
    :param index:
    :param value:
    :return:
    '''
    try:
        mylist[index] = value
    except IndexError:
        for _ in range(index - len(mylist) + 1):
            mylist.append(None)
        mylist[index] = value


def list_unique(mylist: list):
    result = list()
    for x in mylist:
        if x not in result:
            result.append(x)
    return result


def list_rstrip(mylist: list, val):
    # case 1: empty list
    if not mylist:
        return list()

    # case 2: last item != val (for a efficiency return)
    if mylist[-1] != val:
        return mylist

    # case 3: remove all items of "val" from the last item of my-list
    i = 0
    for item in reversed(mylist):
        if item != val:
            break
        i += 1
    return mylist[: -i]
