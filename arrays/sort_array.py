# Check if an Array is Sorted
# arr[] = [10, 20, 30, 5, 6]
def isSorted(nums_arr):
    sortedArr = []
    n = len(nums_arr)
    for i in range(1, n):
        if nums_arr[i - 1] < nums_arr[i]:
            sortedArr.append(nums_arr[i - 1])
    return sortedArr


# calling

arr = [10, 20, 30, 40, 50]
print(isSorted(arr))
print(isSorted([10, 20, 30, 60, 50]))
