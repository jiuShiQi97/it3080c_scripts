#coding: utf-8
import pygame
from sys import exit
from pygame.locals import *
import random

# Set the game screen size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800
#button.py


import pygame.font

# The bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(bull, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(bull)
        bull.image = bullet_img
        bull.rect = bull.image.get_rect()
        bull.rect.midbottom = init_pos
        bull.speed = 10

    def move(bull):
        bull.rect.top -= bull.speed
# The button got in the way during playtesting,
# so I decided to get rid of it (> V <)
# class Button():
#     def __init__(self, ai_settings, screen, msg):
#         #init button
#         self.screen = screen
#         self.screen_rect = screen.get_rect()
#
#         #set button size
#         self.width, self.height = 200, 50
#         self.button_color = (0, 250, 0)
#         self.text_color = (255, 255, 255)
#         self.font = pygame.font.SysFont(None, 48)
#
#         # create rect and make it  mediate
#         self.rect = pygame.Rect(0, 0, self.width, self.height)
#         self.rect.center = self.screen_rect.center
#
#
#         # only one button
#         self.prep_msg(msg)
#
#
#     def prep_msg(self, msg):
#
#         self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
#         self.msg_image_rect = self.msg_image.get_rect()
#         self.msg_image_rect.center = self.rect.center
#
#     def draw_button(self):
#         self.screen.fill(self.button_color, self.rect)
#         self.screen.blit(self.msg_image, self.msg_image_rect)


# Player
class Player(pygame.sprite.Sprite):
    def __init__(player, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(player)
        # A list to store pictures of the player's planes
        player.image = []
        for i in range(len(player_rect)):
            player.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        # Initializes the rectangle in which the image resides
        player.rect = player_rect[0]
        # Initializes the upper-left coordinate of the rectangle
        player.rect.topleft = init_pos
        # Initializes the player's plane speed.
        player.speed = 8
        # The collection of bullets fired by the player's aircraft
        player.bullets = pygame.sprite.Group()
        # Whether the player is hit or not
        player.is_hit = False

    # shoot bullets
    def shoot(shot, bullet_img):
        bullet = Bullet(bullet_img, shot.rect.midtop)
        shot.bullets.add(bullet)

    # Moving up, need to judge the boundary
    def moveUp(shot):
        if shot.rect.top <= 0:
            shot.rect.top = 0
        else:
            shot.rect.top -= shot.speed

    # Moving down, need to judge the boundary
    def moveDown(shot):
        if shot.rect.top >= SCREEN_HEIGHT - shot.rect.height:
            shot.rect.top = SCREEN_HEIGHT - shot.rect.height
        else:
            shot.rect.top += shot.speed

    # Moving left, need to judge the boundary
    def moveLeft(shot):
        if shot.rect.left <= 0:
            shot.rect.left = 0
        else:
            shot.rect.left -= shot.speed

    # Moving right, need to judge the boundary
    def moveRight(shot):
        if shot.rect.left >= SCREEN_WIDTH - shot.rect.width:
            shot.rect.left = SCREEN_WIDTH - shot.rect.width
        else:
            shot.rect.left += shot.speed

# enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(enem, enemy_img, enemy_down_imgs, init_pos):
       pygame.sprite.Sprite.__init__(enem)
       enem.image = enemy_img
       enem.rect = enem.image.get_rect()
       enem.rect.topleft = init_pos
       enem.down_imgs = enemy_down_imgs
       enem.speed = 2

    # enemy move
    def move(enem):
        enem.rect.top += enem.speed

# init pygame
pygame.init()

# Set the size of the game interface, background image and title
# Pixel size of the game interface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# caption
pygame.display.set_caption('Python Star Wars')

# bg
background = pygame.image.load('resources/image/background.png').convert()

# Game Over img
game_over = pygame.image.load('resources/image/gameover.png')

# plane and bullets
plane_img = pygame.image.load('resources/image/shoot.png')

# Set up a list of pictures of the player's aircraft in different states.
# Multiple pictures are displayed as animations.
player_rect = []
player_rect.append(pygame.Rect(0, 99, 100, 121))
player_rect.append(pygame.Rect(165, 234, 102, 126))

player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)

# bullet img
bullet_rect = pygame.Rect(68, 75, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

# List of pictures of enemy planes in different states
enemy1_rect = pygame.Rect(534, 612, 53, 40)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = plane_img.subsurface(pygame.Rect(267, 347, 57, 43))


# Stores enemy planes and manages multiple objects
enemies1 = pygame.sprite.Group()

# Stores destroyed enemy
enemies_down = pygame.sprite.Group()

# Initialize firing and enemy movement frequency
shoot_frequency = 0
enemy_frequency = 0

# score
score = 0
# fps
clock = pygame.time.Clock()
# exit?
running = True

# main
# Add bgm
pygame.mixer.music.load("resources/bgm/bgm.mp3")
# play music!
pygame.mixer.music.play()
while running:
    # max fps = 60
    clock.tick(60)

    # Generate bullets, need to control the firing frequency
    # First determine that the player's plane was not hit
    # Loops 15 times = 1 bullet
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    # Generate enemy aircraft, need to control the generation frequency
    # Loop 50 times to generate 10 more enemy
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 2
    if enemy_frequency >= 100:
        enemy_frequency = 0

    for bullet in player.bullets:
        # bullet move
        bullet.move()
        # remove bullet
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)   

    for enemy in enemies1:
        #2. move enemy
        enemy.move()
        #3. Collisions between enemy planes and player planes
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            break
        #4. Remove enemies after moving off the screen
        if enemy.rect.top < 0:
            enemies1.remove(enemy)

    # The effects of enemy planes being hit by bullets
    # Adds the hit enemy object to the Kill Enemy Group
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    # draw bg
    screen.fill(0)
    screen.blit(background, (0, 0))
    # Add game icon
    #!!!!I don't know why I add icon and this game frames are not stable !!!!
    #image = pygame.image.load('resources/image/icon.ico')
    #pygame.display.set_icon(image)

    # draw player
    if not player.is_hit:
        screen.blit(player.image[0], player.rect) # draw normal plane
    else:
        # player's plane is hit
        screen.blit(player.image[1], player.rect) # draw a boom
        running = False

    # enemy is hit
    for enemy_down in enemies_down:
        enemies_down.remove(enemy_down)
        score += 1
        #draw a boom
        screen.blit(enemy_down.down_imgs, enemy_down.rect)


    # draw bullet
    player.bullets.draw(screen)
    # draw enemy
    enemies1.draw(screen)

    # score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render('score: '+str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [200, 10]
    screen.blit(score_text, text_rect)

    # reflesh
    pygame.display.update()

    # exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # KeyListener
    key_pressed = pygame.key.get_pressed()

    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()

# Game Over and show score
font = pygame.font.Font(None, 64)
text = font.render('Final Score: '+ str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
# Score's location
text_rect.centery = screen.get_rect().centery + 150
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)

# show score and exit
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()