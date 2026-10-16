def PrimeChecker(num):
    if num <= 1:
        return "Not prime"
    for i in range (2, num):
        if num % i == 0:
            return "Not prime"
    return "Prime"

InputNum = int(input("Enter a number: "))
print(PrimeChecker(InputNum))