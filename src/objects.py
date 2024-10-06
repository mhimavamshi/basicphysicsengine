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

        

        for force in self.forces:
            self.acceleration += force.scale(1 / self.mass)

        self.velocity += self.acceleration.scale(delta_time)
        self.position += self.velocity.scale(delta_time)   
        self.momentum = self.velocity.scale(self.mass)
        self.forces = []

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    @abstractmethod
    def world_bounds_position(self):
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

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.position.to_pygamevec(), self.radius)

    # def __str__(self):
    #     return super().__str__()

    def out_of_bounds(self, bounds):
        pass

