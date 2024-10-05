from abc import ABC, abstractmethod
import random
import pygame

class PhysicsEngine:
    def __init__(self, *kwargs):
        self.objects = []

    def register(self, object):
        self.objects.append(object)
    
    def run(self, delta_time):
        for object in self.objects:
            object.update(delta_time)
            # TODO: handle collisions etc

    def draw_objects(self, screen):
        for object in self.objects:
            object.draw(screen)
    
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.direction = (self.x, self.y)
    
    def __add__(self, vector):
        return Vector(vector.x + self.x, vector.y + self.y)
    
    def __sub__(self, vector):
        return Vector(vector.x - self.x, vector.y - self.y)
    
    def scale(self, value):
        return Vector(self.x * value, self.y * value)

    def to_pygamevec(self):
        return pygame.Vector2(self.x, self.y)

class RandomVector(Vector):
    def __init__(self, x_bounds, y_bounds):
        super().__init__(random.uniform(*x_bounds), random.uniform(*y_bounds))

    

# refactor later
class PhysicsObject:
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def update(self, delta_time):
        pass

class Circle(PhysicsObject):
    def __init__(self, position, radius, color="black"):
        super().__init__(position)
        self.radius = radius
        self.color = color
        self.velocity = None

    def add_velocity(self, velocity):
        self.velocity = velocity
    
    def update(self, delta_time):
        if self.velocity:
            self.position += self.velocity.scale(delta_time)    

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.to_pygamevec(), self.radius)
