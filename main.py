import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # Player.__init__ must add itself to these
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
