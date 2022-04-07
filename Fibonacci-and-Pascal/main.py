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

# Write tests for printNumbers() function

def test_printNumbers():
    assert printNumbers(8)       == '1 4 3'
    assert printNumbers(89)      == '1 9 28 35 15 1'
    assert printNumbers(610)     == '1 13 66 165 210 126 28 1'
    assert printNumbers(10_946)  == '1 19 153 680 1820 3003 3003 1716 495 55 1'
    assert printNumbers(317_811) == '1 26 300 2024 8855 26334 54264 77520 75582 48620 19448 4368 455 14'

    print("Tests Succeeded!")

test_printNumbers()