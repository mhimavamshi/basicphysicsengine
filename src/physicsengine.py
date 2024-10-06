from src.objects import *
import pygame

class PhysicsEngine:
    def __init__(self, **kwargs):
        self.objects: list[PhysicsObject] = []
        self.should_log = True
        self.id_counter = 0
        self.x_limit = kwargs['x_limit']
        self.y_limit = kwargs['y_limit']
        self.world_bounds = (self.x_limit, self.y_limit) 

    def register(self, object: PhysicsObject) -> None:
        object.id = self.id_counter
        self.objects.append(object)
        self.id_counter += 1

    def log(self, string, logtype="[INFO]"):
        if self.should_log: print(logtype, string)

    def out_of_bounds(self, object):
        return object.position.x >= self.x_limit or object.position.y >= self.y_limit or object.position.x <= 0 or object.position.y <= 0 

    def run(self, delta_time: float) -> None:
        for object in self.objects:
            object.update(delta_time)
            # TODO: handle collisions etc
            if self.out_of_bounds(object):
                # reverse_force = object.acceleration.scale(-1).scale(object.mass * 3)
                # object.apply_force(reverse_force)
                self.log(str(object)+" collided with wall")
                object.reverse_direction()
                # print("forces on the object:", [str(force) for force in object.forces])


    def draw_objects(self, screen: pygame.Surface) -> None:
        for object in self.objects:
            object.draw(screen)