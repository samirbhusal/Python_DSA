arr = [-9, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

maxVal = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maxVal:
        maxVal = arr[i]
print('maxValue:', maxVal)
