import pygame
from src.physicsengine import *
from src.vector import RandomVector
import random
import math

pygame.init()
WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = "black"
NUMBER_OF_CIRCLES = 3
MASS_PER_AREA = 3
clock = pygame.time.Clock()
physics_engine = PhysicsEngine(x_limit = WIDTH, y_limit = HEIGHT) # TODO: provide configs like what collider to use, etc etc
delta_time = 0

# RADIUS = 30
# circle = Circle(Vector(WIDTH / 2, HEIGHT / 2), RADIUS) # create a circle object at the centre of screen
# circle.add_velocity(RandomVector(x_bounds=(0, 100), y_bounds=(0, 100))) # add a velocity vector
# circle2 = Circle(Vector(0, HEIGHT / 2), RADIUS, color="red")
# circle2.add_velocity(Vector(10, 20))
# physics_engine.register(circle) # add circle to be managed by engine
# physics_engine.register(circle2)

color_list = list(pygame.color.THECOLORS.keys())
color_list.remove(BACKGROUND_COLOR)
circles = []
for i in range(NUMBER_OF_CIRCLES):
    radius = random.randint(10, 40)
    mass = math.pi * (radius ** 2) * MASS_PER_AREA
    circle = Circle(RandomVector((radius, WIDTH / 2), (radius, HEIGHT / 2)), mass, radius, color=random.choice(color_list))
    circle.apply_force(RandomVector((-10, 20),  (-30, 40)).scale(mass))
    physics_engine.register(circle)
    circles.append(circle)


# game loop
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False 
    
    SCREEN.fill(BACKGROUND_COLOR)

    physics_engine.run(delta_time)
    physics_engine.draw_objects(SCREEN)
    
    for circle in circles:
        circle.apply_force(RandomVector((-10, 20),  (-30, 40)))

    delta_time = clock.tick(60) / 1000

    pygame.display.flip()
    

pygame.quit()
