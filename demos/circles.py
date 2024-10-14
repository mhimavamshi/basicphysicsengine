import sys
sys.path.append('../')

import pygame
from src.physicsengine import *
from src.vector import RandomVector
import random
import math

pygame.init()


WIDTH, HEIGHT = 1000, 1000
bounds = (WIDTH, HEIGHT)
pygame.display.set_caption("Circles")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = "black"
NUMBER_OF_CIRCLES = 25
MASS_PER_AREA = 5


clock = pygame.time.Clock()

physics_engine = PhysicsEngine(x_limit = WIDTH, y_limit = HEIGHT) # TODO: provide configs like what collider to use, etc etc
delta_time = 0

color_list = list(pygame.color.THECOLORS.keys())
color_list.remove(BACKGROUND_COLOR)
for i in range(NUMBER_OF_CIRCLES):
    radius = random.randint(20, 40)
    mass = math.pi * (radius ** 2) * MASS_PER_AREA
    circle = Circle(RandomVector((0, WIDTH / 2), (0, HEIGHT / 2)), mass, radius, bounds=bounds, color=random.choice(color_list))
    circle.apply_force(RandomVector((-10, 20),  (-30, 40)).scale(mass))
    physics_engine.register(circle)
# radius = 50

# circle1 = Circle(Vector(radius, HEIGHT / 2), 5, radius, color="red")
# circle1.apply_force(Vector(40, 0))
# physics_engine.register(circle1)

# circle2 = Circle(Vector(WIDTH - radius, HEIGHT / 2), 5, radius, color="yellow")
# circle2.apply_force(Vector(-40, 0))
# physics_engine.register(circle2)

# circle3 = Circle(Vector(WIDTH / 2, radius), 5, radius, "green")
# circle3.apply_force(Vector(0, 40))
# physics_engine.register(circle3)

# circle4 = Circle(Vector(WIDTH / 2, HEIGHT - radius), 5, radius, "white")
# circle4.apply_force(Vector(0, -40))
# physics_engine.register(circle4)


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
