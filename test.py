# studentList = [['samir', 78.8], ['bhusal', 99.9], ['Harry',37.21], ['Berry',37.21], ['Tina',37.2]]
studentList = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    studentList.append([name, score])

studentList.sort(key=lambda x: x[1])
for i in range(1, 3):
    print(studentList[i][0])


