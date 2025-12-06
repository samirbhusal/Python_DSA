def findOddEven(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def getMultiplicationTable(n):
    for i in range(1, 11):
        print('%d * %d = %d' % (n, i, i * n))


# Program for sum of n natural numbers
def getSumOfNaturalNumbers(n):
    sumOfNum = 0
    for i in range(1, n + 1):
        sumOfNum += i
    return sumOfNum


# Program for Sum of squares of first n natural numbers
def getSumOfSquaresOfNaturalNumbers(n):
    sumOfNum = 0
    for i in range(1, n + 1):
        sumOfNum += i * i
    return sumOfNum


# Swap Two Numbers
def swapTwoNums(num1, num2):
    num1, num2 = num2, num1
    return num1, num2

# Find Closest to n and Divisible by m
