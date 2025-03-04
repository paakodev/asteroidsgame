from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    # STATE METHODS        
    def update(self, dt):
        self.position += self.velocity * dt
    
    
    # GRAPHICS METHODS    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)