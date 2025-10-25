from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # destroy the asteroid and if its the smallest stop the method
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # get the angle to shoot the asteroid towards
        angle = random.uniform(20, 50)
        pos_dir = self.velocity.rotate(angle)
        neg_dir = self.velocity.rotate(-angle)

        # make the asteroid smaller and shoot them in opposite directions
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity = pos_dir * 1.2
        ast2.velocity = neg_dir * 1.2
