def BinarySearch(lst: list, item):
    # Initialize the lower and upper bounds of the search range
    low = 0
    high = len(lst) - 1

    # Compute the middle index
    mid = (low + high) // 2

    # Guess is the element at the middle index
    guess = lst[mid]

    # Loop while the search range is valid
    while low <= high:
        # Recompute the middle index
        mid = (low + high) // 2
        # Update the guess
        guess = lst[mid]

        # If the guess is the item, return the index
        if guess == item:
            return f"Your item is at index {mid}"
        
        # If the guess is greater than the item, adjust the upper bound
        elif guess > item:
            high = mid - 1

        # If the guess is less than the item, adjust the lower bound
        else:
            low = mid + 1

    # Return None if the item is not found
    return None
