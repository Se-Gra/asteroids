import pygame, sys

from player import Player
from logger import log_state, log_event
from asteroid import Asteroids
from asteroidfield import AsteroidField
from shot import Shot

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroids.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        # game
        updatable.update(dt)
        #print(asteroids)
        for asteroid_ in asteroids:
            if asteroid_.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for object_ in drawable:
            object_.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
