# code your iterative algorithm here
def binary_search(data, el):
    first = 0
    last = len(data) - 1
    found = False

    while first <= last and not found:
        mid = (first+last)//2  # // operator returns an integer value. / returns a floating value. 

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]:
                last = mid-1
            else:
                first = mid+1
    return found

test_list = [5,8,12,14,19,22,27,30,31]

print(binary_search(test_list, 12))
# When the program is run, the output is True. If we change the desired element from 12 to 11, then the output is False.
