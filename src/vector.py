import pygame
import random
import math
import unittest

class Vector:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y
        self.direction = (self.x, self.y)
    
    def __add__(self, vector):
        return Vector(vector.x + self.x, vector.y + self.y)
    
    def __sub__(self, vector):
        return Vector(vector.x - self.x, vector.y - self.y)
    
    def __eq__(self, vector) -> bool:
        return (self.x == vector.x) and (self.y == vector.y)

    def scale(self, value: float):
        return Vector(self.x * value, self.y * value)

    def distance_to(self, vector) -> float:
        return math.sqrt((self.x - vector.x) ** 2 + (self.y - vector.y) ** 2)

    def to_pygamevec(self) -> pygame.Vector2:
        return pygame.Vector2(self.x, self.y)

    def __str__(self):
        return f"Vector: {self.direction}"

class RandomVector(Vector):
    def __init__(self, x_bounds: tuple, y_bounds: tuple):
        super().__init__(random.uniform(*x_bounds), random.uniform(*y_bounds))


class TestVectorMethods(unittest.TestCase):

    def test_distance_to(self):
        v1 = Vector(1, 1)
        v2 = Vector(2, 2)
        self.assertEqual(v1.distance_to(v2), 1.4142135623730951)
        v1 = Vector(-2, 3)
        self.assertEqual(v1.distance_to(v2), 4.123105625617661)
        v1 = Vector(2, 2)
        self.assertEqual(v1.distance_to(v2), 0)

    def test_scaling(self):
        v1 = Vector(2, 2)
        v2 = Vector(4, 4)
        self.assertEqual(v1.scale(2), v2)

if __name__ == "__main__":
    unittest.main()