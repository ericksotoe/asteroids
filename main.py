import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create a game loop 
    while True:
        # for mac use, stops game when x bubble is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # create a blank black screen
        screen.fill(color=(0,0,0))
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
