def Factorial(n):
    # Calculate the factorial of a number using recursion
    if n > 1:
        return n * Factorial(n-1)
    else:
        return 1  # Base case: factorial of 1 or 0 is 1

def Fibonacci(n):
    # Calculate the nth Fibonacci number using recursion
    if n > 1:
        return Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return n  # Base cases: Fibonacci(0) = 0, Fibonacci(1) = 1

def ListSum(lst):
    # Calculate the sum of a list of numbers using recursion
    if len(lst) > 0:
        return lst[0] + ListSum(lst[1:])
    else:
        return 0  # Base case: sum of an empty list is 0

def ReverseString(text):
    # Reverse a string using recursion
    if len(text) > 0:
        return text[-1] + ReverseString(text[:-1])
    else:
        return ""  # Base case: reversing an empty string yields an empty string

def Power(a, b):
    # Calculate a to the power of b using recursion
    if b >= 1:
        return a * Power(a, b-1)
    else:
        return 1  # Base case: any number to the power of 0 is 1

def BinarySearch(lst, target, low, high):
    # Perform a binary search on a sorted list using recursion
    mid = (low + high) // 2

    if low > high:
        return "Your item is not in the list."  # Base case: target is not found

    if lst[mid] == target:
        return f"Your item is at index {mid}"  # Base case: target is found
    elif target > lst[mid]:
        return BinarySearch(lst, target, mid+1, high)  # Search in the right half
    elif target < lst[mid]:
        return BinarySearch(lst, target, low, mid-1)  # Search in the left half

def GreatestCommonDivisor(a, b):
    # Calculate the greatest common divisor (GCD) of two numbers using recursion
    if b == 0:
        return a  # Base case: GCD(a, 0) is a
    else:
        return GreatestCommonDivisor(b, a % b)  # Recursive case: GCD(a, b) = GCD(b, a % b)

def ListMax(lst):
    # Find the maximum value in a list using recursion
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]  # Base case: return the larger of two elements
    
    sub_max = ListMax(lst[1:])  # Recursive case: find the maximum in the rest of the list
    return lst[0] if lst[0] > sub_max else sub_max  # Return the larger of the first element and the sub_max

def ListCount(lst):
    # Count the number of elements in a list using recursion
    if lst == []:
        return 0  # Base case: an empty list has 0 elements
    else:
        return 1 + ListCount(lst[1:])  # Recursive case: count the first element and the rest of the list
