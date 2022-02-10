# Name: Jacob Trentini
# School: Stratford Middle School, Pleasanton.
# Program: Fibonacci Clock
# Year: 2021 -22
# Honor Code : "I pledge that I have upheld the Stratford honor code in letter and in spirit."

import time

indexToTimeAdded = {0: 1,
									  1: 1,
										2: 2,
										3: 3,
										4: 5}

def formulateMinutes(minutes: int) -> str:
	if minutes >= 10: return str(minutes)
	return "0" + str(minutes)


def findTime(c1, c2, c3, c4, c5):
	startingTime = time.time()
	hours   = 0
	minutes = 0
	userInput = [c1, c2, c3, c4, c5]

	for index, letter in enumerate(userInput):
		if letter == "R" or letter == "B":
			hours += indexToTimeAdded[index]

		if letter == "G" or letter == "B":
			minutes += indexToTimeAdded[index]
	
	print((time.time() - startingTime) * 100_000)
	
	if hours < 10: print("0", end="")
	print(hours, end=":")
	print(formulateMinutes(minutes * 5))

findTime("R", "W", "G", "B", "G")
findTime("W", "B", "B", "G", "R")
findTime("R", "W", "G", "B", "G")

# def calculateFibClock(userInput: [str]):
# 	hours   = 0
# 	minutes = 0

# 	for index, letter in enumerate(userInput):
# 		if letter == "R" or letter == "B":
# 			hours += indexToTimeAdded[index]

# 		if letter == "G" or letter == "B":
# 			minutes += indexToTimeAdded[index]
	
# 	if hours < 10: print("0", end="")
# 	print(hours, end=":")
# 	print(formulateMinutes(minutes * 5))


# userInput1 = input("Enter an input: ").upper().split(" ")
# userInput2 = input("Enter an input: ").upper().split(" ")
# userInput3 = input("Enter an input: ").upper().split(" ")
# userInput4 = input("Enter an input: ").upper().split(" ")
# userInput5 = input("Enter an input: ").upper().split(" ")

# calculateFibClock(userInput1)
# calculateFibClock(userInput2)
# calculateFibClock(userInput3)
# calculateFibClock(userInput4)
# calculateFibClock(userInput5)