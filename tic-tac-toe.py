import pygame
pygame.init()

size = (600, 400)
pygame.display.set_mode(size)
pygame.display.set_caption("tic-tac-toe")
img = pygame.image.load("image_tictactoe.jpg")
pygame.display.set_icon(img)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
