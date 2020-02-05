import pygame


def turn_frame(char, side):
    # TURN IMAGE
    char.side = side
    if char.can_turn:
        if char.side == 'right':
            char.turn = True
        else:
            char.turn = False
