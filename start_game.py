import pygame
from music import Music, Sound
import sys
from main_menu import MainMenu
from settings import Settings
from choose_fighter_host import ChooseFighterH
from choose_fighter_client import ChooseFighterC
from egg import Egg
from connect_to_server import Connect
from fight import Fight

pygame.init()
pygame.mixer.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

fall = 1
pygame.time.set_timer(fall, 10)
fps = 80
clock = pygame.time.Clock()

settings = {'music': 1, 'sound': 1}

setting_music = ['Музыка: вкл',
                 'Звуки: вкл']

gold_egg = '0'
m = Music()
s = Sound()
current_menu = MainMenu()
while True:
    t = current_menu.run()
    if t[0] == 'settings':
        current_menu = Settings(m, s)
    elif t[0] == 'main':
        current_menu = MainMenu()
    elif t[0] == 'start fight':
        current_menu = Fight(t[1])
    elif t[0] == 'connect to server':
        current_menu = Connect()
    elif t[0] == 'legendary_egg':
        current_menu = Egg()
    elif t[0] == 'choose fighter h':
        current_menu = ChooseFighterH()
    elif t[0] == 'choose fighter c':
        current_menu = ChooseFighterC(t[1])
    elif t[0] == 'exit':
        print('exit')
        sys.exit()
