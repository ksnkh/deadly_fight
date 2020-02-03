import pygame
from music import Music, Sound
from load_image import load_image
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
hero_creator = 'джонни'
hero_guest = 'джонни'
main_map = ''

setting_music = ['Музыка: вкл',
                 'Звуки: вкл']

gold_egg = '0'
m = Music()
s = Sound()
m.play()
current_menu = MainMenu()
while True:
    t = current_menu.run()
    if t == 'settings':
        current_menu = Settings(m, s)
    elif t == 'main':
        current_menu = MainMenu()
    elif t == 'start fight':
        current_menu = Fight()
    elif t == 'connect to server':
        current_menu = Connect()
    elif t == 'legendary_egg':
        current_menu = Egg()
    elif t == 'choose fighter h':
        current_menu = ChooseFighterH()
    elif t == 'choose fighter c':
        current_menu = ChooseFighterC()


