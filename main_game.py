import pygame 
import sys;
from random import randint;

pygame.init()

screen = pygame.display.set_mode((800, 600)); 

pygame.display.set_caption("My game");


screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))

pygame.display.update();

while True: 
    for event in  pygame.event.get(): 
        if(event.type == pygame.QUIT): 
            sys.exit();