import sys, pygame, random, pandas as pd
from ship import Ship
from asteroid import Asteroid
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()
#set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w * 0.5), int(screen_info.current_h *))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
screen.fill(color)

#read and store game data
df = pd.read_csv("game_info.csv")

#setup game variables
asteroid = pygame.sprite.Group()
numLevels = df["LevelNum"].max()
level = df["LevelNum"].min()
levelData = df.iloc[level]
asteroidCount = levelData["AsteroidCount"]
player = Ship((levelData["PlayerX"], levelData["PlayerY"]))

def init():
    global asteroidCount, asteroids, levelData
    levelData = df.iloc[level]
    player.reset((levelData["PlayerX"], levelData["PlayerY"]))
    asteroids.empty()
    asteroidCount = levelData["AsteroidCount"]
    for i in range(asteroidCount):
        asteroids.add(Asteroid((random.randint(50, width-50)), random.randint(15, 60)))

def win():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You have passed the asteroid belt, you are now safe!", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        screen.fill(color)
        assert isinstance(text_rect,)
        screen.blit(text, text_rect)
        pygame.display.flip()