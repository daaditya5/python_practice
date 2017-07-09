test_cases = int(input().strip())
for i in range((test_cases)):
    number = int(input().strip())
    number = bin(number)
    print(number[2:])

