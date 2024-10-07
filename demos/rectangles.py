import sys
sys.path.append('../')

import pygame
from src.physicsengine import *
from src.vector import RandomVector
import random
import math

pygame.init()


WIDTH, HEIGHT = 1000, 1000
pygame.display.set_caption("Rectangles")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = "black"
MASS_PER_AREA = 3
NUMBER_OF_RECTS = 10


clock = pygame.time.Clock()

physics_engine = PhysicsEngine(x_limit = WIDTH, y_limit = HEIGHT) # TODO: provide configs like what collider to use, etc etc
delta_time = 0

rectangles = []
for i in range(NUMBER_OF_RECTS):
    RECT_WIDTH = random.randint(3, 5)
    RECT_HEIGHT = random.randint(4, 8)
    area = RECT_WIDTH * RECT_HEIGHT
    mass = MASS_PER_AREA * area
    rectangle = Rectangle(RandomVector((RECT_WIDTH + 1, WIDTH - RECT_WIDTH * 2), (RECT_HEIGHT + 1, HEIGHT - RECT_HEIGHT * 2)), 5, (50, 50), "white")
    rectangle.apply_force(RandomVector((-5, 10),  (-10, 5)).scale(mass))
    physics_engine.register(rectangle)

# game loop
running = True 
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False 
    
    SCREEN.fill(BACKGROUND_COLOR)

    physics_engine.run(delta_time)
    physics_engine.draw_objects(SCREEN)

    delta_time = clock.tick(60) / 1000

    pygame.display.flip()
    

pygame.quit()
