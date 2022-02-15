# Implementation of binary search algorithm

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# binary search uses divide and conqure

def binary_search(l, target, high=None, low=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low : # if target is not in the list
        return -1
    middle_value = (low + high)//2
    if l[middle_value] == target:
        return middle_value
    elif target < l[middle_value]:
        return binary_search(l, target, low, middle_value - 1)
    else: # target > l[middle_value]
        return binary_search(l, target, middle_value + 1, high)
if __name__=="__main__":
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))