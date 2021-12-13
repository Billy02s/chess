import pygame
from piece import Bishop
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()
screen_size = 800
board = pygame.display.set_mode((screen_size,screen_size))
pygame.display.set_caption("Chess")
pygame.display.update()

black = (112, 79, 54)
white = (199, 153, 117)

fps = 60
    
def draw_board():
    tile = screen_size/8
    count = 2

    for i in range(0,8):
        for j in range(0,8):
            if count % 2 == 0:
                pygame.draw.rect(board, white, [tile*j, tile*i, tile, tile])
            else:
                pygame.draw.rect(board, black, [tile*j, tile*i, tile, tile])
            count += 1
        count -= 1

    b = Bishop(0,0,"black")
    b.draw(board)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    draw_board()
    
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == MOUSEBUTTONDOWN:
                pass

    pygame.quit()

if __name__ == "__main__":
    main()

