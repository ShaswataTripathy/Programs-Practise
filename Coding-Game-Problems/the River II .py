
#A digital river is a sequence of numbers where every number is followed by
#the same number plus the sum of its digits. In such a sequence 123 is
#followed by 129 (since 1 + 2 + 3 = 6), which again is followed by 141.

#We call a digital river river K, if it starts with the value K.
#For example, river 7 is the sequence beginning with {7, 14, 19, 29, 40, 44, 52, ... }
#and river 471 is the sequence beginning with {471, 483, 498, 519, ... }.

#Digital rivers can meet. This happens when two digital rivers share
#the same values. River 32 meets river 47 at 47, while river 471 meets river 480 at 519.

#Given a number decide, whether it can be a meeting point of two or more digital rivers. For example, it is easy to check that only river 20 contains the number 20 in its sequence (as a starting point).

#Input
#Line 1: An integer r1.
#Output
#Line 1 : YES if r1 can be a meeting points of two digital rivers, NO otherwise.


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def getNextRiverNumber(riverNumber):
    nextRiverNumber = riverNumber

    while riverNumber > 0:
        nextRiverNumber += riverNumber % 10
        riverNumber -= riverNumber % 10
        riverNumber /= 10

    return nextRiverNumber

r_1 = int(input())

riversMeetR1 = False

#Find rivers that meet r1.
for i in range(r_1 - 1, 0, -1):
    riversMeetR1 = (getNextRiverNumber(i) == r_1)
    if riversMeetR1:
        break

#Output if other rivers meet r1.
print("YES" if riversMeetR1 else "NO")