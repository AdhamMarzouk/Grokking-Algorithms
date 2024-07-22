def QuickSort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]

        smaller = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]

        return QuickSort(smaller) + [pivot] + QuickSort(greater)