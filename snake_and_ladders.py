import pygame
import sys

pygame.font.init()
height = 500
width = 500
cell_size = width//10
font = pygame.font.Font('freesansbold.ttf', 12)


def draw_board(screen):
    next_num = cell_size
    x = 5
    y = 455
    color = [(255, 255, 255), (255, 182, 193)]
    for i in range(11):
        for j in range(11):
            pygame.draw.rect(screen, color[(i+j) % 2], (cell_size*i, cell_size*j, cell_size, cell_size))
    for i in range(100):
        number = font.render(f"{i+1}", True, (0, 0, 0))
        screen.blit(number, (x, y))
        x = x + next_num
        j = (i // 10) % 2
        if j == 0 and i == (10*(i//10))+9:
            y = y-cell_size
            x = 455
            next_num = -cell_size
        elif j == 1 and i == (10*(i//10))+9:
            y = y - cell_size
            x = 5
            next_num = cell_size


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_board(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
