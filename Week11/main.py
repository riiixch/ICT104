# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1


def search(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


# Driver Code
arr = [22, 80, 42, 44, 99, 11, 2, 18, 35, 60]
x = 44
n = len(arr)

# Function call
result = search(arr, n, x)

print("==========")
print("Array :", arr)
print("Sequential Search :", x)

if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)

print("65064435 สมภพ เอี่ยมสมบัติ")
print("==========")  



# Python3 Program for recursive binary search.
# Returns index of x in arr if present, else -1

def binarySearch(arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Driver Code
arr = [22, 80, 42, 44, 99, 11, 2, 18, 35, 60]
x = 45

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

print("==========")
print("Array :", arr)
print("Binary Search :", x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

print("65064435 สมภพ เอี่ยมสมบัติ")
print("==========")