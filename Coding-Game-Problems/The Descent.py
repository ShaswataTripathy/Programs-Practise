#Destroy the mountains before your starship collides with one of them. For that, shoot the highest mountain on your path.
#Rules
#At the start of each game turn, you are given the height of the 8 mountains from left to right.
#By the end of the game turn, you must fire on the highest mountain by outputting its index (from 0 to 7).

#Firing on a mountain will only destroy part of it, reducing its height. Your ship descends after each pass.

#Victory Conditions
#You win if you destroy every mountain

#Lose Conditions
#Your ship crashes into a mountain
#You provide incorrect output or your program times out

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    max = 0
    maxIndex = -1

    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        #Set highest mountain.
        if mountain_h > max:
            max = mountain_h
            maxIndex = i

    print(maxIndex)