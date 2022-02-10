# ACSL-Fibonacci-Clock 2021-2022
First competition program for ACSL 2021-2022 done through Tech Club

[Repl.it Link](https://replit.com/join/hfousaeghp-squealingfur185)

## Problem

ACSL’s version of Philippe Chretien’s “Fibonacci Clock” displays time by changing the colors displayed in 5 squares, whose side lengths
correspond to the first 5 Fibonacci numbers (1, 1, 2, 3, and 5). Given the colors of the squares on the clock face, you must output the time that is represented in hh:mm format. The colors will be given to you as 5 individual characters representing the lower 1x1
square, the upper 1x1 square, the 2x2 square, the 3x3 square, and the 5x5 square in that order. (See https://basbrun.com/2015/05/04/fibonacci-clock/.)

## Square Representation
- Red squares are used to represent only hours and green squares are used to represent only minutes.
- Blue squares are used to represent both hours and minutes. White squares are ignored. 

> To find the current hour, add the values of the red and blue squares. To find the current minutes, add the values of the green and blue squares and multiply by 5. The minutes are displayed in five-minute increments.

## Fibonacci Clock Example

![Fibonacci Clock Example](https://github.com/Awesomeplayer165/ACSL-Fibonacci-Clock/blob/440920eef955fb38466583213b1784ed03e41811/Fibonacci-Clock-Example.png)

The clock in the picture above is displaying 08:50. The hours are represented by the red 1x1, blue 2x2, and blue 5x5 squares (1+2+5=8).
The minutes are represented by the blue 2x2, the green 3x3, and the blue 5x5 squares (2+3+5=10 and 10*5=50).

The example at the left which uses the inputted characters R, W, G, B, G displays the time 04:50.
The hours are represented by the 1x1 red square and the 3x3 blue square: 1+3=4. The minutes are represented by the 2x2 green, the 3x3 blue, and the 5x5 green squares: (2+3+5)*5 = 50.
The example at the right which uses the inputted characters: W, B, B, G, R displays the time 08:30.
The hours are 1+2+5=8 and the minutes are (1+2+3)*5=30.

![Fibonacci Clock Left](https://github.com/Awesomeplayer165/ACSL-Fibonacci-Clock/blob/440920eef955fb38466583213b1784ed03e41811/Left-Image-Example.png)                   ![Fibonacci Clock Right](https://github.com/Awesomeplayer165/ACSL-Fibonacci-Clock/blob/440920eef955fb38466583213b1784ed03e41811/Left-Image-Example.png)

## Input

There are 5 sets of data. Each set has 5 uppercase letters (R, G, B, or W) that represent
the colors of the lower 1x1, the upper 1x1, the 2x2, the 3x3, and finally the 5x5 square, in that
order. We guarantee that the input will represent a valid time from 00:00 to 11:55.

## Output

For each line of data, print the time in hours and minutes formatted as hh:mm.

## Sample 1 Input and Output

| Input     | Output   |
|-----------|----------|
| R W G B G | 1. 04:50 |
| W B B G R | 2. 08:30 |
| B G B B R | 3. 11:35 |
| W W W B B | 4. 08:40 |
| W R G G G | 5. 01:50 |

## Sample 2 Input and Output

| Input     | Output   |
|-----------|----------|
| G R W B B | 1. 09:45 |
| R B B W G | 2. 04:40 |
| W W W W W | 3. 00:00 |
| B W W G R | 4. 06:20 |
| W B B B B | 5. 11:55 |

## Created and Maintained by:

[Jacob Trentini](https://github.com/Awesomeplayer165)
