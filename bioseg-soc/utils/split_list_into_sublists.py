def split_list_into_sublists(lst, size=10):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]