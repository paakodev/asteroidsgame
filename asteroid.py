from circleshape import *
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # STATE METHODS
    def move(self, dt):
        self.position += self.velocity * dt
        
    def update(self, dt):
        self.move(self, dt)
    
    
    # GRAPHICS METHODS    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 2)