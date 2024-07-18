def BinarySearch(lst: list, item):
    low = 0
    high = len(lst) - 1

    mid = (low + high) // 2

    guess = lst[mid]

    while low <= high:
        
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == item:
            return f"Your item is at index {mid}"
        
        elif guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None

