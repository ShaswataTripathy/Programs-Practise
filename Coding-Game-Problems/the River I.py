#A digital river is a sequence of numbers where every number is followed by the same number plus the sum of its digits.
#In such a sequence 123 is followed by 129 (since 1 + 2 + 3 = 6), which again is followed by 141.
#We call a digital river river K, if it starts with the value K.
#For example, river 7 is the sequence beginning with {7, 14, 19, 29, 40, 44, 52, ... }
#and river 471 is the sequence beginning with {471, 483, 498, 519, ... }.

#Digital rivers can meet. This happens when two digital rivers share the same values.
#River 32 meets river 47 at 47, while river 471 meets river 480 at 519.
#Given two meeting digital rivers print out the meeting point.

#Input
#Line 1: The first river r1.
#Line 2: The second river r2.
#Output
#Line 1 : The meeting point of the rivers given.

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def getNextRiverNumber(riverNumber):
    nextRiverNumber = riverNumber

    while riverNumber > 0:
        nextRiverNumber += riverNumber % 10
        riverNumber -= riverNumber % 10
        riverNumber //= 10

    return nextRiverNumber

r1 = int(input())
r2 = int(input())

while r1 != r2:
    if r1 < r2:
        r1 = getNextRiverNumber(r1)
    else:
        r2 = getNextRiverNumber(r2)


print(r1)