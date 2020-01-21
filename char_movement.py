import pygame


def gravity(fighter):
    fighter.vector[1] += 0.6


def move(fighter, shift):
    if fighter.ducked or fighter.block or fighter.attack:
        return
    if fighter.on_ground and not fighter.getting_damage:
        fighter.vector[0] = 4 * shift


def jump(fighter):
    if fighter.ducked or fighter.block or fighter.attack:
        return
    if fighter.on_ground:
        if fighter.vector[0]:
            fighter.vector[1] -= 28
        else:
            fighter.vector[1] -= 28
        fighter.vector[0] *= 2
        fighter.on_ground = 0
