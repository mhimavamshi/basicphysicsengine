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

    # def out_of_bounds(self, object):
        # return object.position.x >= self.x_limit or object.position.y >= self.y_limit or object.position.x <= 0 or object.position.y <= 0 

    def run(self, delta_time: float) -> None:


        for object in self.objects:
            object.update(delta_time)
            # TODO: handle collisions etc
                # self.log(f"{str(object)} has acceleration of {object.acceleration}")
            # collision with the "walls"
            # if object.is_out_of_bounds(self.world_bounds):
                # self.log(str(object)+" collided with wall at "+str(object.position))
                # object.correct_bounds()
                # object.reverse_direction()

        done = [[False for _ in range(len(self.objects))] for _ in range(len(self.objects))]
        for i, first_object in enumerate(self.objects):
            for j, second_object in enumerate(self.objects):
                if i == j or done[i][j] or done[j][i]:
                    continue
                
                if isinstance(first_object, Circle) and isinstance(second_object, Circle) and first_object.is_colliding_with(second_object):
                    self.log(f"{first_object} colliding with {second_object}, mass: {first_object.mass} and acceleration: {first_object.acceleration}")
                    
                    normal = (second_object.position - first_object.position).scale(1 / first_object.position.distance_to(second_object.position))
                    
                    relative_velocity = second_object.velocity - first_object.velocity
                    
                    vel_along_normal = relative_velocity.dot(normal)
                    
                    if vel_along_normal > 0:
                        continue
                    
                    e = 0.9
                    
                    cj = -(1 + e) * vel_along_normal / (1 / first_object.mass + 1 / second_object.mass)
                    
                    first_object.velocity += normal.scale(cj / first_object.mass)
                    second_object.velocity -= normal.scale(cj / second_object.mass)
                    
                    done[i][j] = True
                    done[j][i] = True




    def draw_objects(self, screen: pygame.Surface) -> None:
        for object in self.objects:
            object.draw(screen)