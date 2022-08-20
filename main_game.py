""" Velikus Arena main game interface
    version: 0.1
    Code: gpizzigh-bit
    co: Marlon Dinis
    Art: Matheus Vincentini
"""

import sys
from tkinter import font
from turtle import Screen
import pygame
import sys


pygame.init()
pygame.display.set_caption('Velikus Arena v0.1')
screen = pygame.display.set_mode((1280, 720),0,32)
mainClock = pygame.time.Clock()

font_path = "H:\Velikus_Arena\Assets\Fonts\masque.ttf"
smallTitle = pygame.font.Font(font_path,25)
mediumTitle = pygame.font.Font(font_path,45)
bigTitle = pygame.font.Font(font_path,100)
darkgreen = (28,106,39)

def draw_text(text, font, color, surface, x, y) :
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

click = False

def main_menu() :
    click = False
    while True :
        screen.fill((255,255,255))
        draw_text("Velikus Arena",bigTitle,darkgreen,screen,162,136)

        mx, my = pygame.mouse.get_pos()

        button_start = pygame.Rect(391,370,498,64)
        button_quit = pygame.Rect(391,507,498,64)

        pygame.draw.rect(screen,darkgreen ,button_start)
        pygame.draw.rect(screen,darkgreen ,button_quit)

        if button_start.collidepoint((mx,my)):
            if click:
                game()
        if button_quit.collidepoint((mx,my)):
            if click:
                pygame.quit()
                sys.exit()

        draw_text("Start",mediumTitle,(255,255,255),screen,558,372)
        draw_text("Quit",mediumTitle,(255,255,255),screen,577,509)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type  == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    click = True
            
        pygame.display.update()
        mainClock.tick(60)

def game():
    click = False
    while True :
        screen.fill((255,255,255)) # fill screen white for new screen

        for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)

main_menu()
