import pygame
import os

pygame.init()
width,height = 800, 800
board = pygame.display.set_mode((width,height))
pygame.display.set_caption("Chess")
pygame.display.update()

piece_width, piece_height = 100, 100


wpawn_image = pygame.image.load('assets/wPawn.png')
wpawn = pygame.transform.scale(wpawn_image, (piece_width, piece_height))
bpawn_image = pygame.image.load('assets/bPawn.png')
bpawn = pygame.transform.scale(bpawn_image, (piece_width, piece_height))

black = (112, 79, 54)
white = (199, 153, 117)

fps = 60

def draw_board():
    tile = 100
    board.fill(white)

    count = 2

    for i in range(0,8):
        for j in range(0,8):
            if count % 2 == 0:
                pygame.draw.rect(board, white, [tile*j, tile*i, tile, tile])
            else:
                pygame.draw.rect(board, black, [tile*j, tile*i, tile, tile])
            count += 1
        count -= 1

    pygame.draw.rect(board, black, [tile,tile,8*tile,8*tile],1)
    

    board.blit(wpawn,(200, 590))
    board.blit(bpawn,(200,0))
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

    pygame.quit()

if __name__ == "__main__":
    main()

