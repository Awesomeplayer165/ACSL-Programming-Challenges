# get input

userInput: [str] = input("Enter an input: ").split(", ")

# decide type of cell operation

class Operations:
    
    @staticmethod
    def divide(cell: str):
        print(f"{cell[:4]*2} and {cell[4:]*2}")

    @staticmethod
    def add(n: int, cell: str):
        print(cell[:n] + cell[:-n if n > 0 else 8])

    @staticmethod
    def subtract(n: int, cell: str):
        print(cell[n:] + cell[-n if n > 0 else 8 :])
    

if   userInput[0]     == "DIVIDE":   Operations.divide(                         userInput[1])
elif userInput[0][:3] == "ADD":      Operations.add     (int(userInput[0][-1]), userInput[1])
elif userInput[0][:8] == "SUBTRACT": Operations.subtract(int(userInput[0][-1]), userInput[1])
