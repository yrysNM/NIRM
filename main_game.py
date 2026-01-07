import pygame 
import sys;
from random import randint;

pygame.init()
pygame.display.set_caption("My game");

screen_width, screen_height = 800, 600;
screen = pygame.display.set_mode((screen_width, screen_height)); 
clock = pygame.time.Clock();
fill_color = (32, 52, 71);

rect_width, rect_height = 100, 200; 
rect_x = screen_width / 2 - rect_width / 2;
rect_y = screen_height / 2 - rect_height / 2;
rect_color = pygame.Color("lightyellow")

STEP = 10;


while True: 
    for event in  pygame.event.get():
        eventType = event.type;         
        if(eventType == pygame.QUIT): 
            sys.exit();
        if(eventType == pygame.KEYDOWN): 
            eventKey = event.key;
            if(eventKey == pygame.K_UP and rect_y >= STEP): 
                rect_y -= STEP
            if(eventKey == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP): 
                rect_y += STEP
            if(eventKey == pygame.K_LEFT and rect_x >= STEP): 
                rect_x -= STEP;
            if(eventKey == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP): 
                rect_x += STEP;
    
    screen.fill(fill_color);
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height));
    pygame.display.update();


    # screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
    # pygame.display.update();
    # clock.tick(5)
            
        