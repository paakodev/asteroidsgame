import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()  # No arguments needed here
        # After init, add self to each container
        if hasattr(self.__class__, "containers"):
            for container in self.__class__.containers:
                container.add(self)
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    def collision(self, other):
        dist = self.position.distance_to(other.position)
        if dist > (self.radius + other.radius):
            return False
        
        return True

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass