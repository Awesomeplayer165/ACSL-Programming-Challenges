# get input

class CellOperations:
    
    # solve - String Manipulation 

    @staticmethod
    def divide(cell: str):
        print(f"{cell[:4]*2} and {cell[4:]*2}")

    @staticmethod
    def add(n: int, cell: str):
        print(cell[:n] + cell[:-n if n > 0 else 8])

    @staticmethod
    def subtract(n: int, cell: str):
        print(cell[n:] + cell[-n if n > 0 else 8 :])
    
# decide type of cell operation

for i in range(0, 5):
    userInput: [str] = input("Enter an input: ").split(", ")

    if   userInput[0]     == "DIVIDE":   CellOperations.divide(                         userInput[1])
    elif userInput[0][:3] == "ADD":      CellOperations.add     (int(userInput[0][-1]), userInput[1])
    elif userInput[0][:8] == "SUBTRACT": CellOperations.subtract(int(userInput[0][-1]), userInput[1])
