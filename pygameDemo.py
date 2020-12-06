import pygame, sys
from pygame.locals import *

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
screen = pygame.display.set_mode((500, 500))
screen.fill(WHITE)
pygame.display.set_caption("Example")

# Creating Lines and Shapes
pygame.draw.line(screen, BLUE, (150, 200), (130, 170))
pygame.draw.line(screen, BLUE, (150, 130), (170, 170))
pygame.draw.line(screen, GREEN, (130, 170), (170, 170))
pygame.draw.circle(screen, BLACK, (100, 50), 30)
circle = pygame.draw.circle(screen, BLACK, (200, 50), 30)
pygame.draw.rect(screen, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(screen, BLACK, (110, 260, 80, 5))
 
# Beginning Game Loop
while True:
    # print(circle)
    # print(circle.center)
    # print(circle.w)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)
