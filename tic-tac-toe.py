import pygame
import sys

pygame.init()

SIZE_BLOCK = 100
MARGIN = 15
DISPLAY_SIZE = (800, 800)
WHITE_RGB = (255, 255, 255)
BLACK_RGB = (0, 0, 0)
width = height = SIZE_BLOCK*3 + MARGIN*4
arr = [[0]*3 for i in range(3)]

screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("tic-tac-toe")
img = pygame.image.load("image_tictactoe.png")
pygame.display.set_icon(img)
font = pygame.font.SysFont('futura', 32)
welcome_text = font.render("Let's play!", 1, WHITE_RGB, BLACK_RGB)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(welcome_text, (330, 60))
    pygame.display.update()

    for row in range(3):
        for col in range(3):
            x = 230 + col*SIZE_BLOCK + (col+1)*MARGIN
            y = 200 + row*SIZE_BLOCK + (row+1)*MARGIN
            pygame.draw.rect(screen, WHITE_RGB, (x, y, SIZE_BLOCK, SIZE_BLOCK))
    pygame.display.update()