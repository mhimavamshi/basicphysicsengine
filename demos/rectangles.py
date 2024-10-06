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

clock = pygame.time.Clock()

physics_engine = PhysicsEngine(x_limit = WIDTH, y_limit = HEIGHT) # TODO: provide configs like what collider to use, etc etc
delta_time = 0

rectangle = Rectangle(Vector(WIDTH / 2, HEIGHT / 2), 5, (50, 50), "white")
rectangle.apply_force(Vector(10, 10).scale(5))
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
