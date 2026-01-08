import pygame

from player import Player
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, LINE_WIDTH

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        # game
        player.update(dt)
        player.draw(screen, "white", player.triangle(), LINE_WIDTH)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
