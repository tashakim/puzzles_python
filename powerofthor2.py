import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  

    move = 'N' if light_y < initial_ty else 'S' if light_y > initial_ty else ''
    move += 'E' if light_x > initial_tx else 'W' if light_x < initial_tx else ''

    if('N' in move):
    	initial_ty -= 1
    if('S' in move):
    	initial_ty += 1
    if('E' in move):
    	initial_tx += 1
    if('W' in move):
    	initial_tx -= 1

    print(move)