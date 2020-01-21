import pygame
from music import Music, Sound, Music_Flex
from load_image import load_image
from main_menu import MainMenu
from settings import Settings
from fight import Fight
from server import select_fighter
from connect_to_server import Connect
from egg import Egg

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
#n = Music_Flex()
m.play()
mainC = MainMenu()
settingsC = Settings(m, s)
server = Connect()
fightC = Fight()
fighterC = select_fighter()
current_menu = mainC
eggC = Egg(0)
while True:
    t = current_menu.run()
    if t == 'settings':
        current_menu = settingsC
    elif t == 'main':
        current_menu = mainC
    elif t == 'fight':
        current_menu = fightC
    elif t == 'connect to server':
        current_menu = fighterC
        current_menu = server
    elif t == 'legendary_egg':
        current_menu = eggC

