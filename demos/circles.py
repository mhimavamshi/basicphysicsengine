import sys
sys.path.append('../')

import pygame
from src.physicsengine import *
from src.vector import RandomVector
import random
import math

pygame.init()


WIDTH, HEIGHT = 1000, 1000
pygame.display.set_caption("Circles")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = "black"
NUMBER_OF_CIRCLES = 30
MASS_PER_AREA = 3


clock = pygame.time.Clock()

physics_engine = PhysicsEngine(x_limit = WIDTH, y_limit = HEIGHT) # TODO: provide configs like what collider to use, etc etc
delta_time = 0

color_list = list(pygame.color.THECOLORS.keys())
color_list.remove(BACKGROUND_COLOR)
for i in range(NUMBER_OF_CIRCLES):
    radius = random.randint(10, 40)
    mass = math.pi * (radius ** 2) * MASS_PER_AREA
    circle = Circle(RandomVector((radius, WIDTH / 2), (radius, HEIGHT / 2)), mass, radius, color=random.choice(color_list))
    circle.apply_force(RandomVector((-10, 20),  (-30, 40)).scale(mass))
    physics_engine.register(circle)

# game loop
running = True 
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False 
    
    SCREEN.fill(BACKGROUND_COLOR)

    physics_engine.run(delta_time)
    physics_engine.draw_objects(SCREEN)
    
    for circle in physics_engine.objects:
        circle.apply_force(RandomVector((-10, 20),  (-30, 40)))

    delta_time = clock.tick(60) / 1000

    pygame.display.flip()
    

pygame.quit()
