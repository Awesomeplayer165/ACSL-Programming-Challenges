# ACSL Time Sheets with Swift


[ACSL Time Sheets](https://github.com/Awesomeplayer165/ACSL-Time-Sheets-with-Swift/blob/master/TimeSheets%20(2).doc) is a program designed to calculate the daily pay for each employee.

## Problem:

Most hourly paying jobs require someone to enter information on a time sheet. The ACSL Amusement Park is open from 9:00 a.m. to 5:00 p.m. The Business Office enters a code representing the location where an employee works and the starting time and ending time for each day. The codes entered are as follows:

| Time     | Value |
|----------|-------|
| 9:00 AM  | 1     |
| 9:30 AM  | 2     |
| 10:00 AM | 3     |
| 10:30 AM | 4     |
| 11:00 AM | 5     |
| 11:30 AM | 6     |
| 12:00 PM | 7     |
| 1:00 PM  | 8     |
| 1:30 PM  | 9     |
| 2:00 PM  | A     |
| 2:30 PM  | B     |
| 3:00 PM  | C     |
| 3:30 PM  | D     |
| 4:00 PM  | E     |
| 4:30 PM  | F     |
| 5:00 PM  | G     |
| 5:30 PM  | H     |

## Instructions

- Locations 1-9 get paid $10.00 per hour with no overtime for extra hours.
- Locations 10-19 get paid $8.00 per hour for the first 4 hours and $12.00 for any hours over 4.
- Locations 20-29 get $12.00 per hour for the first 4 hours and double that for any hours over 4.

### Input:

There will be 4 lines of input. Each line will contain 3 characters representing the location, start time
and end time for an employee.

### Output: 

For each input line print the daily pay for the employee. The fifth output will be the sum of the four
daily pay amounts. All pay amounts must be printed in dollar and cents format.

## Sample Outputs:

### INPUT #1
1. 5, 9, H
2. 11, 1, 7
3. 19, 3, F
4. 25, 2, B

### OUTPUT #1
1. $40.00
2. $24.00
3. $56.00
4. $60.00
5. $180.00

***

### INPUT #2
1. 3, 9, H
2. 17, 1, E
3. 20, 5, G
4. 15, 2, 8

### OUTPUT #2
1. $40.00
2. $62.00
3. $84.00
4. $24.00
5. $210.00

## REPL:

Visit the Replit link here: https://replit.com/@Squealingfur185/ACSL-Time-Sheets-with-Swift-1#main.swift

## Created and Maintained by:

[Jacob Trentini](https://github.com/Awesomeplayer165)
