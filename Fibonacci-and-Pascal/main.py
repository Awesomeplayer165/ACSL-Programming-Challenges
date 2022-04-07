#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'printNumbers' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER fibNumber as parameter.
#

# generate the fibonacci sequence in the form of a list

fibList = [0, 1]
for i in range(2, 31):
    fibList.append(fibList[i-1] + fibList[i-2])


def getRowElements(row: int) -> [int]:
    rowItems = [1, row]

    decreasingNumerator = rowItems[1]
    increasingDenominator = 2

    for i in range(row - 1):
        rowItems.append(round(rowItems[-1] * ((decreasingNumerator - 1) / increasingDenominator)))
        decreasingNumerator -= 1
        increasingDenominator += 1

    return rowItems

    
def getNumberOfItemsInDiagonal(row: int) -> int:
    return int(row/2) + (1 if row %2 != 0 else 0)

    
def printNumbers(fibNumber):

    row = fibList.index(fibNumber)
    diagonalItems = []
    count = 0

    for i in range(row-1, 0, -1):

        if len(getRowElements(i)) <= count: break

        diagonalItems.append(getRowElements(i)[count])
        count += 1

    return ' '.join(map(str, diagonalItems))

    
print(printNumbers(8))