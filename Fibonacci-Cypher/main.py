# h ACSL c2

userInput = input("Enter input: ")
offset = userInput[0]
message = userInput[2:]

fibonacci_numbers = [0, 1]
for i in range(2,700):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

del fibonacci_numbers[0:2]

for index, char in enumerate(message):
    fibNum = fibonacci_numbers[index]
    offsetDecoded = ord(offset)

    if offsetDecoded + fibonacci_numbers[index] >= 122:
        offsetDecoded = 78

    print(f"Offset ASCII Code: {offsetDecoded + fibonacci_numbers[index]}")