#3 find lowest value in array/list
arr = [10,30,1,20,3,13,17,0]
minValue = arr[0]

for i in arr:
    if i < minValue:
        minValue = i
        print(minValue)

print("Lowest value in a list / array: ", minValue)