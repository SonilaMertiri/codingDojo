# 1.Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!

def pushFront(arr, value):
    return [value] + arr

print(pushFront([5, 7, 2, 3], 8))  # Output: [8, 5, 7, 2, 3]
print(pushFront([99], 7))           # Output: [7, 99]

# 2.Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!
def popFront(arr):
    if len(arr) == 0:
        return None  # If array is empty, return None

    first_value = arr[0]
    arr = arr[1:]
    print(first_value, "returned, with", arr, "printed in the function")
    return first_value

# Examples
print(popFront([0, 5, 10, 15]))  # Output: 0 returned, with [5, 10, 15] printed in the function
print(popFront([4, 5, 7, 9]))    # Output: 4 returned, with [5, 7, 9] printed in the function

# 3.Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!
def insertAt(arr, index, value):
    arr = arr[:index] + [value] + arr[index:]
    return arr

# Examples
print(insertAt([100, 200, 5], 2, 311))  # Output: [100, 200, 311, 5]
print(insertAt([9, 33, 7], 1, 42))      # Output: [9, 42, 33, 7]

# 4.Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).

def removeAt(arr, index):
    if index < 0 or index >= len(arr):
        return None  # If index is out of range, return None

    removed_value = arr.pop(index)
    print(removed_value, "returned, with", arr, "printed in the function")
    return removed_value

# Examples
print(removeAt([1000, 3, 204, 77], 1))  # Output: 3 returned, with [1000, 204, 77] printed in the function
print(removeAt([8, 20, 55, 44, 98], 3))  # Output: 44 returned, with [8, 20, 55, 98] printed in the function

# 4.Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.
def swapPairs(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Examples
print(swapPairs([1, 2, 3, 4]))         # Output: [2, 1, 4, 3]
print(swapPairs(["Brendan", True, 42]))# Output: [True, "Brendan", 42]

# 5.Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!
def removeDupes(arr):
    if len(arr) <= 1:
        return arr
    
    unique_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_arr.append(arr[i])
    
    return unique_arr

# Examples
print(removeDupes([-2, -2, 3.14, 5, 5, 10]))   # Output: [-2, 3.14, 5, 10]
print(removeDupes([9, 19, 19, 19, 19, 19, 29]))# Output: [9, 19, 29]
