import pygame


def gravity(fighter):
    fighter.vector[1] += 0.3


def move(fighter, shift):
    if fighter.on_ground:
        fighter.vector[0] = 3 * shift


def jump(fighter):
    if fighter.on_ground:
        if fighter.vector[0]:
            fighter.vector[1] -= 13
        else:
            fighter.vector[1] -= 11
        fighter.vector[0] *= 1.5
        fighter.on_ground = 0
