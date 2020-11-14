import sys, pygame
import os

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

# rules

clock = pygame.time.Clock()

x = 100
y = 180
speed = (0, 0)
attackA = False
attackB = False
attackC = False
attackD = False
walkCount = 0
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
RED = (255,0,0)
GREEN = (0,255,0)

# Screen Display
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
bg_imgBat = pygame.image.load("battle.png")
bg_batt = pygame.transform.scale(bg_imgBat, (width, height))

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

player_health = 100
# Colors
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
white = (255, 255, 255)
black = (0, 0, 0)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Redraw
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def redrawGameWindow():
    global walkCount

    screen.blit(bg_batt, (0, 0))

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


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Main Loop
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
run = True
while run:
    clock.tick(27)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Keys
    # --------------------------------------------
    pygame.draw.rect(screen, RED, (420,150,100,5))
    pygame.draw.rect(screen, GREEN, (120, 150, player_health, 5))
    key = pygame.key.get_pressed()
    play_rect = play_rect.move(speed)
    if key[pygame.K_UP]:
        player_health = - 5
        play_rect = play_rect.move([0, 0])
        attackA = True
        attackB = False
        attackC = False
        attackD = False

    if key[pygame.K_DOWN]:
        play_rect = play_rect.move([0, 0])
        attackA = False
        attackB = True
        attackC = False
        attackD = False
    if key[pygame.K_LEFT]:
        play_rect = play_rect.move([0, 0])
        attackA = False
        attackB = False
        attackC = True
        attackD = False
    if key[pygame.K_RIGHT]:
        play_rect = play_rect.move([0, 0])
        attackA = False
        attackB = False
        attackC = False
        attackD = True






    # --------------------------------------------

    redrawGameWindow()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
