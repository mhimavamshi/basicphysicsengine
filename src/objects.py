from abc import ABC, abstractmethod
from src.vector import Vector
import pygame

# refactor later
class PhysicsObject:
    # def __init__(self, position: Vector, mass: float, velocity: Vector = Vector(0, 0), acceleration: Vector = Vector(0, 0)):
    def __init__(self, position: Vector, mass: float, force: Vector = Vector(0, 0)):
        self.mass = mass
        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.momentum = self.velocity.scale(self.mass)
        # self.force = self.acceleration.scale(self.mass)
        self.force = force
        self.forces = [self.force]
        self.name = "PhysicsObject"
        self.id = -1

    def __str__(self):
        return f"NAME: {self.name} ID: {self.id}"

    @abstractmethod
    def apply_force(self, force: Vector):
        self.forces.append(force)

    @abstractmethod
    def reverse_direction(self):
        self.acceleration = self.acceleration.scale(-1)
        self.velocity = self.velocity.scale(-1)

    @abstractmethod
    def update(self, delta_time: float):
        # self.acceleration = Vector(0, 0)

        if self.forces:
            for force in self.forces:
                self.acceleration += force.scale(1 / self.mass)
            self.forces = []

        self.velocity += self.acceleration.scale(delta_time)
        self.position += self.velocity.scale(delta_time)   
        self.momentum = self.velocity.scale(self.mass)

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    @abstractmethod
    def is_out_of_bounds(self, bounds: tuple) -> bool:
        pass

    @abstractmethod
    def correct_bounds(self) -> bool:
        pass

    # def add_acceleration(self, acceleration: Vector):
    #     self.acceleration = acceleration

    # def add_velocity(self, velocity: Vector):
    #     self.velocity = velocity


class Circle(PhysicsObject):
    def __init__(self, position: Vector, mass: float, radius: float, color: str = "black"):
        super().__init__(position, mass)
        self.name = "Circle"
        self.radius = radius
        self.color = color

        self.bound_calc_cache = [0, 0, 0, 0]

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.position.to_pygamevec(), self.radius)

    # def __str__(self):
    #     return super().__str__()

    # def correct_bounds(self) -> bool:
    #     if self.bound_calc_cache[0]:
    #         self.position.x -= self.radius
    #     if self.bound_calc_cache[1]:
    #         self.position.y -= self.radius
    #     if self.bound_calc_cache[2]:
    #         self.position.x += self.radius
    #     if self.bound_calc_cache[3]:
    #         self.position.y += self.radius
    
    def is_out_of_bounds(self, bounds: tuple) -> bool:
        # greater_x_out = self.position.x > bounds[0] - self.radius 
        # greater_y_out = self.position.y > bounds[1] - self.radius 
        # lesser_x_out = self.position.x < self.radius 
        # lesser_y_out = self.position.y < self.radius 
        # self.bound_calc_cache = [greater_x_out, greater_y_out, lesser_x_out, lesser_y_out]
        # return any(self.bound_calc_cache)
        return self.position.x >= bounds[0] - self.radius or self.position.y >= bounds[1] - self.radius or self.position.x <= self.radius or self.position.y <= self.radius 
