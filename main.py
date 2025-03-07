import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    ok, failed = pygame.init()
    print(f"OK: {ok}\t\tFAILED: {failed}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill("black")
        updatable.update(dt)
        
        for roid in asteroids:
            if player.collision(roid):
                print("Game over!")
                pygame.quit()
        
        for roid in asteroids:
            for shot in shots:
                if roid.collision(shot):
                    roid.split()
                    shot.kill()
                
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        
        # Tick the loop
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
