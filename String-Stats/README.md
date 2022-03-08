# ACSL String Stats

A Practice Coding Challenge for ACSL

## Problem

Given a sentence (up to 1024 characters long), output the following:

1. The number of different letters. This will be a number from 1 to 26, inclusive
2. The number of vowels. Vowels are the letters "a, e, i, o, and u."
3. The number of uppercase letters
4. The number of times that the most frequent letter appears. There is no distinction between lowercase and uppercase letters
5. The longest word in the sentence. If there is a tie, print one that appears first when sorting these words alphabetically without regard to lowercase and uppercase.

## Input

One line of data, containing a sentence, up to 1024 characters long.

## Output

Print the five statistics specified above in that order.

### Sample Input

The quick brown fox, named Roxanne, jumped over Bruno, a lazy dog.

### Sample Output

1. 25
2. 19
3. 3
4. 6
5. Roxanne

### Test Input 1

The 2019 All-Star Competition is at the Wayne Hills HS in Wayne, New Jersey.

### Test Output 1

1. 16
2. 19
3. 11
4. 7
5. Competition
