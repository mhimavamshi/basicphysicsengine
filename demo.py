import pygame
from src.physicsengine import *

pygame.init()
WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = "white"
clock = pygame.time.Clock()
physics_engine = PhysicsEngine() # TODO: provide configs like what collider to use, etc etc
delta_time = 0

RADIUS = 30
circle = Circle(Vector(WIDTH / 2, HEIGHT / 2), RADIUS) # create a circle object at the centre of screen
circle.add_velocity(RandomVector(x_bounds=(0, 100), y_bounds=(0, 100))) # add a velocity vector
physics_engine.register(circle) # add circle to be managed by engine

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
