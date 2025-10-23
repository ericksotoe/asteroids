import pygame
from player import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create groups for drawable and updatable obj
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # create player sprite
    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # create a game loop 
    while True:
        # for mac use, stops game when x bubble is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # create a blank black screen
        updatable.update(dt)
        screen.fill(color=(0,0,0))

        # draw each item in the group individually
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
