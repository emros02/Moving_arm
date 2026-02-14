#Projekt_1 - Emilia Mrosek, Katarzyna Koszacka, Julia Turulska
import os
import math
from sys import exit
import pygame

os.environ['SDL_VIDEO_CENTERED']='1'

#basic settings
width, height = 800, 600
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Double Pendulum")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#objects
circle_color = (230, 170, 90)
line_color = (255, 200, 120)
circle_radius = 7
line_width = 15
icon = pygame.image.load('head.png')
hand = pygame.image.load('hand.png')
diamond = pygame.image.load('diamond.png')

#resize hand_img
hand_scale=0.5
hand_width, hand_height = hand.get_size()
new_hand_width = hand_scale*hand_width
new_hand_height = hand_scale*hand_height
hand = pygame.transform.scale(hand, (new_hand_width, new_hand_height))

#resize icon
icon_scale=0.7
icon_width, icon_height = icon.get_size()
new_icon_width = icon_scale*icon_width
new_icon_height = icon_scale*icon_height
icon = pygame.transform.scale(icon, (new_icon_width, new_icon_height))

#resize diamond
diamond_scale=0.35
diamond_width, diamond_height = diamond.get_size()
new_diamond_width = diamond_scale*diamond_width
new_diamond_height = diamond_scale*diamond_height
diamond = pygame.transform.scale(diamond, (new_diamond_width, new_diamond_height))

#variables
arm_length1 = 100
arm_length2 = 70
angle1 = -math.pi/2
angle2 = math.pi
angle3 = math.pi/8
speed1 = (math.pi/100)
speed2 = (math.pi/60)
speed3 = (math.pi / 60)
middle_point = (width/2, height/2)
diamond_point = (width/2, height/2- 70)

icon_width, icon_height = icon.get_size()
x0=middle_point[0]+icon_width/2 -20
y0=middle_point[1]+icon_height/2 - 5


#setting hand wave
hand_wave = True

running = True

#main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255,255,230))

    #icon
    icon_rect = icon.get_rect(center=middle_point)
    screen.blit(icon, icon_rect)

    #diamond
    diamonod_rect = diamond.get_rect(midbottom=diamond_point)
    screen.blit(diamond, diamonod_rect)

    # setting position of next circles
    x1 = float(x0 + arm_length1 * math.cos(angle1))
    y1 = float(y0 + arm_length1 * math.sin(angle1))

    x2 = float(x1 + arm_length2 * math.cos(angle2))
    y2 = float(y1 + arm_length2 * math.sin(angle2))

# ----------------------------------------------------------------------------

    #lines and circles
    pygame.draw.line(screen, line_color, (x0, y0), (x1, y1), line_width)
    pygame.draw.line(screen, line_color, (x1, y1), (x2, y2), line_width)
    pygame.draw.circle(screen, circle_color, (x0, y0), circle_radius)
    pygame.draw.circle(screen, circle_color, (x1, y1), circle_radius)
    pygame.draw.circle(screen, circle_color, (x2, y2), circle_radius)

    #pivot
    pivot = (hand.get_width() / 2 -50, hand.get_height()-40)
    rotated_hand = pygame.transform.rotate(hand, math.degrees(angle3))
    rotated_rect = rotated_hand.get_rect()
    pivot_vector = pygame.math.Vector2(pivot)
    rotated_pivot = pivot_vector.rotate(-math.degrees(angle3))
    rotated_rect.center = (int(x2+5 - rotated_pivot.x + pivot[0]), int(y2-40 - rotated_pivot.y + pivot[1]))

    screen.blit(rotated_hand, rotated_rect)

    # movement
    if angle1 % (2 * math.pi) < 3 * math.pi / 2:
        speed1 *= -1
    else:
        pass

    if angle2 % (2 * math.pi) - math.pi / 2 < math.pi / 2:
        speed2 *= -1
    else:
        pass

    angle1 += speed1
    angle2 += speed2

    if angle3 % (2*math.pi) > math.pi/4:
        speed3 *= -1
    else:
        pass
    angle3 -= speed3
#---------------------------------------------------------
    keys = pygame.key.get_pressed()

    #changing rotation of first arm
    #key_left => change of direction
    if keys[pygame.K_LEFT]: angle1 -= 2*speed1
    #key_right => stop
    if keys[pygame.K_RIGHT]: angle1 -= speed1
    #key_up => two times faster
    if keys[pygame.K_UP]: angle1 += speed1
    #key_up => two times slower
    if keys[pygame.K_DOWN]: angle1 -= speed1/2

    # changing rotation of second arm
    # key_a => change of direction
    if keys[pygame.K_a]: angle2 -= 2 * speed2
    # key_d => stop
    if keys[pygame.K_d]: angle2 -= speed2
    # key_w => two times faster
    if keys[pygame.K_w]: angle2 += speed2
    # key_s => two times slower
    if keys[pygame.K_s]: angle2 -= speed2/ 2

    #key space => arm is straight
    if keys[pygame.K_SPACE]: angle2= angle1

    if keys[pygame.K_RSHIFT]: angle3 += speed3

    pygame.display.flip()
    clock.tick(60)

pygame.quit()