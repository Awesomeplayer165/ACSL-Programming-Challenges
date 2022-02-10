
# The dealer must play a card of the same suit if he can. 

# He plays the lowest card in that suit that is of a higher rank than the card the opponent played.

# If he does not have such a card, he plays his lowest card in that suit.

# Examples:
# Input: 5,D,2,D,6,H,9,D,9,S,6,H - Output: 9,D
# Input: 4,C,1,C,6,C,7,H,5,S,4,D - Output: 6,C

def getInput() -> str:
	userInput = input("Enter input: ")

	userInput.replace(" ", "")
	userInput = userInput.split(",")
	
	return userInput

class Card:
	number = 0
	suit   = ""

	def __init__(self, number, suit):
		self.number = number
		self.suit == suit

def decodeInput(userInput):
	
	cards: [Card] = []

	for index, item in enumerate(userInput):
		if index > 2 and index %2 != 1:
			cards.append(Card(userInput[index-1], item))
	
	for item in cards:
		print(item.number)
		print(item.suit)



userInput = getInput()
decodeInput(userInput)