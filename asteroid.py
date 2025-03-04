from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # STATE METHODS        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(angle)
        new_vector_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_roid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_roid_1.velocity = new_vector_1 * 1.2
        new_roid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_roid_2.velocity = new_vector_2 * 1.2
    
    # GRAPHICS METHODS    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)