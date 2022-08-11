import pygame

pygame.init()
# https://www.youtube.com/watch?v=jO6qQDNa2UY     [14:03]
game_window = pygame.display.set_mode((900,800))
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()