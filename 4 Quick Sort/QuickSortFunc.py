def QuickSort(lst):
    # Base case: A list with fewer than 2 elements is already sorted
    if len(lst) < 2:
        return lst
    else:
        # Choose the first element as the pivot
        pivot = lst[0]

        # Create a sublist of all elements smaller than or equal to the pivot
        smaller = [i for i in lst[1:] if i <= pivot]
        # Create a sublist of all elements greater than the pivot
        greater = [i for i in lst[1:] if i > pivot]

        # Recursively sort the sublists and combine them with the pivot
        return QuickSort(smaller) + [pivot] + QuickSort(greater)
