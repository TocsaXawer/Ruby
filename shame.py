import pygame, sys
import random
import math
from Run import Run

pygame.init()

screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("Space Invaders")

score = 0

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0.1

enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 1

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10

bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 33, y + 10))
    
def is_collision():
    global enemyX
    global enemyY
    global bulletX
    global bulletY
    
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY + bulletY, 2)))
    if distance < 150:
        return True
    else:
        return False
        


running = True

while running:

    screen.fill((200, 100, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Run()




    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -5
        if event.key == pygame.K_RIGHT:
            playerX_change = 5
        if event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
    
    
    
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    player(playerX, playerY)

    enemy(enemyX, enemyY)

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyY += enemyY_change
        enemyX_change = 1.5
    elif enemyX >= 740:
        enemyY += enemyY_change
        enemyX_change = -1.5
        
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    collision = is_collision()
   
    if collision:
       bulletY = 480
       bullet_state = "ready"
       score += 1
       print(score)
       enemyX = random.randint(0,800)
       enemyY = random.randint(50, 150)

    pygame.display.update()
