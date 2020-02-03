import pygame
from music import Music, Sound
from load_image import load_image
from main_menu import MainMenu
from settings import Settings
from choose_fighter_host import Fight
from choose_fighter_client import select_fighter
from egg import Egg
from connect_to_server import Connect

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
mainC = MainMenu()
settingsC = Settings(m, s)
fightC = Fight()
server_connectC = Connect()
fighterC = select_fighter()
current_menu = mainC
eggC = Egg()
while True:
    t = current_menu.run()
    if t == 'settings':
        current_menu = settingsC
    elif t == 'main':
        current_menu = mainC
    elif t == 'fight':
        current_menu = fightC
    elif t == 'connect to server':
        print(12)
        current_menu = fighterC
    elif t == 'legendary_egg':
        current_menu = eggC
    elif t == 'server_connect':
        current_menu = server_connectC

