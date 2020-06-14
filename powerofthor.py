import sys
import math

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if(light_x > initial_tx  and light_y == initial_ty):
        initial_tx += 1
        print("E")

    elif(light_x < initial_tx and light_y == initial_ty):
        initial_tx -= 1
        print("W")

    elif(light_x == initial_tx and light_y < initial_ty):
        initial_ty -= 1
        print("N")

    elif(light_x == initial_tx and light_y > initial_ty):
        initial_ty += 1
        print("S")

    elif(light_x > initial_tx and light_y < initial_ty):
        initial_tx += 1
        initial_ty -= 1
        print("NE")

    elif(light_x > initial_tx and light_y > initial_ty):
        initial_tx += 1
        initial_ty += 1
        print("SE")

    elif(light_x < initial_tx and light_y > initial_ty):
        initial_tx -= 1
        initial_ty += 1
        print("SW")
        
    elif(light_x < initial_tx and light_y < initial_ty):
        initial_tx -= 1
        initial_ty -= 1
        print("NW")