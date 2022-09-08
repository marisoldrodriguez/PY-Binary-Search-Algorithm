def recursive_bsearch(list, el):

    if len(list) == 0:
        return False

    else:
        mid = len(list)//2

        if list[mid] == el:
            return True
        else:
            if el < list[mid]:
                return recursive_bsearch(list[:mid-1], el)
            else:
                return recursive_bsearch(list[mid+1:], el)

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(recursive_bsearch(test_list, 30))