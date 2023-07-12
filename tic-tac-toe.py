import pygame
pygame.init()

DISPLAY_SIZE = (800, 800)
WHITE_RGB = (255, 255, 255)
BLACK_RGB = (0, 0, 0)

screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("tic-tac-toe")
img = pygame.image.load("image_tictactoe.jpg")
pygame.display.set_icon(img)
font = pygame.font.SysFont('futura', 32)
welcome_text = font.render("Let's play!", 1, WHITE_RGB, BLACK_RGB)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(welcome_text, (320, 60))
    pygame.display.update()
