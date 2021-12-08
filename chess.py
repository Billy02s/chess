import pygame
import os

pygame.init()
width,height = 1000, 900
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Chess")
pygame.display.update()

piece_width, piece_height = 100, 100

wpawn_image = pygame.image.load('/home/billy/assets/wPawn.png')
wpawn = pygame.transform.scale(wpawn_image, (piece_width, piece_height))
bpawn_image = pygame.image.load('/home/billy/assets/bPawn.png')
bpawn = pygame.transform.scale(bpawn_image, (piece_width, piece_height))


background = (150,150,150)

fps = 60

def draw_window():
    screen.fill(background)
    screen.blit(wpawn,(200, 790))
    screen.blit(bpawn,(200,0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    draw_window()
    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()

