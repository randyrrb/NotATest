
# Setup Python ----------------------------------------------- #
import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

width = 1000
height = 500


# ----------------------------------------
#Window Refresh for player
def redrawGameWindow():
    global walkCount

    if walkCount + 1 >= 27:
        walkCount = 0
    elif attackA:
        screen.blit(attack1[walkCount // 3], (x, y))
        walkCount += 1

    elif attackB:
        screen.blit(attack2[walkCount // 3], (x, y))
        walkCount += 1
    elif attackC:
        screen.blit(attack3[walkCount // 3], (x, y))
        walkCount += 1
    elif attackD:
        screen.blit(attack4[walkCount // 3], (x, y))
        walkCount += 1
    else:
        screen.blit(player, (x, y))

    pygame.display.update()
#Window refresh for slime
def redrawGame():

    global walkCount

    if walkCount + 1 >= 27:
        walkCount = 0
    elif attackA:
        screen.blit(Battack1[walkCount // 3], (x, y))
        walkCount += 1

        screen.blit(Slime1, (x, y))

    pygame.display.update()

# ---------------------


# Loads all images ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# slime attack list
# --------------------------------------------------------------------------------------------------------------------
# slime_jump
from turtle import speed

Battack1 = [pygame.image.load('jump1.png'), pygame.image.load('jump2.png'), pygame.image.load('jump3.png'),
            pygame.image.load('jump4.png'),
            pygame.image.load('jump5.png'), pygame.image.load('jump6.png'), pygame.image.load('jump7.png'),
            pygame.image.load('jump8.png'),
            pygame.image.load('jump9.png'), pygame.image.load('jump10.png'), pygame.image.load('jump11.png'), ]

# sheild attack list
# ---------------------------------------------------------------------------------------------------------------------

# sheild_bash
attack1 = [pygame.image.load('shield1.png'), pygame.image.load('shield2.png'), pygame.image.load('sheild3.png'),
           pygame.image.load('sheild4.png'), pygame.image.load('sheild5.png'), pygame.image.load('sheild6.png'),
           pygame.image.load('sheild7.png'), pygame.image.load('sheild8.png'), pygame.image.load('sheild9.png')]
# sleild_slam
attack2 = [pygame.image.load('slam1.png'), pygame.image.load('slam2.png'), pygame.image.load('slam3.png'),
           pygame.image.load('slam4.png'), pygame.image.load('slam5.png'), pygame.image.load('slam6.png'),
           pygame.image.load('slam7.png'), pygame.image.load('slam8.png'), pygame.image.load('slam9.png'),
           pygame.image.load('slam10.png'), pygame.image.load('slam11.png'), pygame.image.load('slam12.png'),
           pygame.image.load('slam13.png'), pygame.image.load('slam14.png'), pygame.image.load('slam15.png'),
           pygame.image.load('slam16.png'), pygame.image.load('slam17.png')]
# slield_
attack3 = [pygame.image.load('shield1.png'), pygame.image.load('shield2.png'), pygame.image.load('sheild3.png'),
           pygame.image.load('sheild4.png'), pygame.image.load('sheild5.png'), pygame.image.load('sheild6.png'),
           pygame.image.load('sheild7.png'), pygame.image.load('sheild8.png'), pygame.image.load('sheild9.png')]
# sheild_
attack4 = [pygame.image.load('shield1.png'), pygame.image.load('shield2.png'), pygame.image.load('sheild3.png'),
           pygame.image.load('sheild4.png'), pygame.image.load('sheild5.png'), pygame.image.load('sheild6.png'),
           pygame.image.load('sheild7.png'), pygame.image.load('sheild8.png'), pygame.image.load('sheild9.png')]

# player 1
player = pygame.image.load('idle1.png')
play_rect = player.get_rect()

#health------------



player_health = 100
slime_health = 100


#-----------------
RED = (255,0,0)
GREEN = (0,255,0)

#------------------


#enime
Slime1 = pygame.image.load('jump1.png')
slime_rect = Slime1.get_rect()

# ---------------------------------------

clock = pygame.time.Clock()

x = 100
y = 180
speed = (0, 0)
attackA = False
attackB = False
attackC = False
attackD = False
walkCount = 0

# -----------------------------------------
pygame.init()

pygame.display.set_caption('Stachue of Purity')
screen = pygame.display.set_mode((width, height))

bg_img = pygame.image.load("REALstart.png")
bg = pygame.transform.scale(bg_img, (width, height))

bg_information = pygame.image.load("info.png")
bg_info = pygame.transform.scale(bg_information, (width, height))

bg_Village = pygame.image.load('REAlvillage.png')
bg_V = pygame.transform.scale(bg_Village, (width, height))

bg_Battle = pygame.image.load('battle.png')
bg_Bat = pygame.transform.scale(bg_Battle, (width, height))

font = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))

        draw_text('PLAY', font, (0, 0, 0), screen, 183, 300)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(83, 295, 200, 50)
        button_2 = pygame.Rect(710, 295, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                village()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 100, 100), button_1)
        pygame.draw.rect(screen, (255, 100, 100), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def village():
    global click
    screen.fill((0, 0, 0))
    screen.blit(bg_V, (0, 0))

    draw_text('PLAY', font, (0, 0, 0), screen, 183, 300)

    mx, my = pygame.mouse.get_pos()

    button_3 = pygame.Rect(83, 295, 200, 50)

    if button_3.collidepoint((mx, my)):
        if click:
            game()

    pygame.draw.rect(screen, (255, 100, 100), button_3)

    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.display.update()
    mainClock.tick(60)

def game():
    clock.tick(27)
    global play_rect
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_Bat, (0, 0))

    pygame.draw.rect(screen,RED,(200,250,500,5))
    pygame.draw.rect(screen, GREEN, (200, 250, player_health, 5))



    draw_text('ESC to go back', font, (255, 255, 255), screen, 20, 20)
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    key = pygame.key.get_pressed()
    play_rect = play_rect.move(speed)
    if key[pygame.K_q]:
             play_rect = play_rect.move([0, 0])
             attackA = True
             attackB = False
             attackC = False
             attackD = False

    if key[pygame.K_w]:
            play_rect = play_rect.move([0, 0])
            attackA = False
            attackB = True
            attackC = False
            attackD = False
    if key[pygame.K_e]:
            play_rect = play_rect.move([0, 0])
            attackA = False
            attackB = False
            attackC = True
            attackD = False
    if key[pygame.K_r]:
            play_rect = play_rect.move([0, 0])
            attackA = False
            attackB = False
            attackC = False
            attackD = True

        # --------------------------------------------

    redrawGameWindow()
    redrawGame()

    pygame.display.update()
    mainClock.tick(60)



def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg_info, (0, 0))

        draw_text('ESC to go back', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
