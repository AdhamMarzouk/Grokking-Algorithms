def FindSmallest(lst):
    # Initialize the index of the smallest element
    smallest_index = 0
    # Iterate over the list to find the index of the smallest element
    for i in range(len(lst)):
        # If the current element is smaller than the smallest element found so far, update smallest_index
        if lst[i] < lst[smallest_index]:
            smallest_index = i 
    # Return the index of the smallest element
    return smallest_index

def SelectionSort(lst):
    # Initialize a new list to store the sorted elements
    newlst = []
    # Loop until the original list is empty
    while len(lst) > 0:
        # Find the index of the smallest element in the list
        smallest_index = FindSmallest(lst)
        # Append the smallest element to the new list
        newlst.append(lst[smallest_index])
        # Remove the smallest element from the original list
        lst.pop(smallest_index)
    # Return the new list containing the sorted elements
    return newlst
