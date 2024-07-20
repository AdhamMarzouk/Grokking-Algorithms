def Factorial(n):
    if n > 1:
        return n * Factorial(n-1)
    else:
        return 1
    

def Fibonacci(n):
    if n > 1:
        return Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return n
    

def ListSum(lst):
    if len(lst) > 0:
        return lst[0] + ListSum(lst[1:])
    else:
        return 0
    

def ReverseString(text):
    if len(text) > 0:
        return text[-1] + ReverseString(text[:-1])
    else:
        return ""
    

def Power(a, b):
    if b >= 1:
        return a * Power(a, b-1)
    else:
        return 1
    

def BinarySearch(lst, target, low, high):
    mid = (low + high) // 2

    if low > high:
        return "Your item is not in the list."

    if lst[mid] == target:
        return f"Your item is at index {mid}"
    elif target > lst[mid]:
        return BinarySearch(lst, target, mid+1, high)
    elif target < lst[mid]:
        return BinarySearch(lst, target, low, mid-1)
    

def GreatestCommonDivisor(a, b):
    if b == 0:
        return a
    else:
        return GreatestCommonDivisor(b, a%b)