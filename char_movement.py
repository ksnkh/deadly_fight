import pygame


def gravity(fighter):
    fighter.vector[1] += 0.6


def move(fighter, shift):
    if fighter.on_ground:
        fighter.vector[0] = 4 * shift


def jump(fighter):
    if fighter.on_ground:
        if fighter.vector[0]:
            fighter.vector[1] -= 22
        else:
            fighter.vector[1] -= 20
        fighter.vector[0] *= 2
        fighter.on_ground = 0
