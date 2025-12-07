def quickSort(nums):
    if len(nums) <= 1:
        return nums
    nums.sort()
    # Partition:
    pivot = nums.pop()
    lower_items = []
    higher_items = []

    for item in nums:

        if item < pivot:
            lower_items.append(item)
        else:
            higher_items.append(item)
    return quickSort(lower_items) + [pivot] + quickSort(higher_items)


if __name__ == "__main__":
    arr = [5, 11, 2, 4, 6, 8, 10]
    print(quickSort(arr))
