def FindSmallest(lst):
    smallest_index = 0
    for i in range(len(lst)):
        if lst[i] < lst[smallest_index]:
            smallest_index = i 

    return smallest_index

def SelectionSort(lst):
    newlst = []
    while len(lst) > 0:
        smallest_index = FindSmallest(lst)
        newlst.append(lst[smallest_index])
        lst.pop(smallest_index)

    return newlst