#import
import pygame
import random
import time

from pygame.constants import MOUSEBUTTONDOWN
from pygame.time import Clock

pygame.init()

#Colours
LIGHT_BLUE = (160, 200, 250)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Window
WIDTH, HEIGHT = 800, 600
ded = False
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
gameTitle = pygame.display.set_caption("Cookie Clicker")
BackgroundColour = LIGHT_BLUE

#Cookie
MAIN_CHARACTER = pygame.image.load('Cookie.png')

player_x, player_y = pygame.mouse.get_pos()

#Cookie monster
COOKIE_MONSTER =  pygame.image.load('cookieMonster.png')
small_COOKIE_MONSTER = pygame.transform.scale(COOKIE_MONSTER, (64, 64))
cm_X, cm_y = random.randint(0, 746), random.randint(70, 430)
pygame.display.update()

#speed
speed = 5

#Score
score = 0

myFont = pygame.font.Font('freesansbold.ttf', 20)

#music
pygame.mixer.music.load('Background_song.mp3') # import the background music
pygame.mixer.music.play(-1)

#main game loop
while ded == False:

    pygame.time.delay(30)

    gameWindow
    gameWindow.fill(BackgroundColour)
    gameWindow.blit(MAIN_CHARACTER, (player_x, player_y))
    gameWindow.blit(small_COOKIE_MONSTER, (cm_X, cm_y))
    gameTitle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ded = True

        #elif event.type == pygame.MOUSEBUTTONDOWN:
            #player_x, player_y = event.pos
            #if MAIN_CHARACTER.get_rect().collidepoint(player_x, player_y):
                #print("click")

    scoreBoard = "Score: " + str(score)
    scoreText = myFont.render(scoreBoard, 1, WHITE)

    pygame.draw.rect(gameWindow, BLACK, pygame.Rect(0, 500, 800, 100))
    gameWindow.blit(scoreText, (10, 540))

    cookieRect = pygame.Rect(player_x, player_y, 64, 64)
    cookieMonsterRect = pygame.Rect(cm_X, cm_y, 64, 64)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player_x > speed: # left
        player_x -= speed
    elif keys[pygame.K_d] and player_x < WIDTH - 64 : # right
        player_x += speed
    elif keys[pygame.K_w] and player_y > speed: # up
        player_y -= speed
    elif keys[pygame.K_s] and player_y < HEIGHT - 164: # down
        player_y += speed

    if cookieRect.colliderect(cookieMonsterRect):
        score += 1
        speed += 0.5
        cm_X, cm_y = random.randint(0, 746), random.randint(70, 430)
        

    pygame.display.update()
pygame.quit()

