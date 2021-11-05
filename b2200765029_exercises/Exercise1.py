N = int(input("Please enter a number : "))
evenSum = 0
oddSum = 0
for i in range(1, N + 1):
    if i % 2 != 0:
        oddSum = oddSum + i
    else:
        evenSum = evenSum + i
        if N % 2 == 0:
            evenNumbers = N / 2
            average = evenSum / evenNumbers
        else:
            evenNumbers= (N-1) / 2
            average = evenSum / evenNumbers
print("The sum of odd numbers : {0}".format(oddSum))
print("The average of even numbers : {0}".format(average))
