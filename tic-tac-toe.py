import pygame

pygame.init()

# display objects
SIZE_BLOCK = 100
MARGIN = 15
DISPLAY_SIZE = (800, 360)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("tic-tac-toe")
img = pygame.image.load("image-tic-tac-toe.png")
pygame.display.set_icon(img)
game_field = [[0] * 3 for i in range(3)]
query = 0


def check_win(field, sign: str):
    empty_cells = 0
    for row in field:
        empty_cells += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if field[0][col] == sign and field[1][col] == sign and field[2][col] == sign:
            return sign
    if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
        return sign
    if field[0][2] == sign and field[1][1] == sign and field[2][0] == sign:
        return sign
    if empty_cells == 0:
        return "Draw!"
    return False


while True:
    font = pygame.font.SysFont('futura', 42)
    screen.blit(font.render("Let's play!", 1, GREEN, BLACK), (480, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            column = x_mouse // (SIZE_BLOCK + MARGIN)
            row = y_mouse // (SIZE_BLOCK + MARGIN)
            if game_field[row][column] == 0:
                if query % 2 == 0:
                    game_field[row][column] = 'x'
                else:
                    game_field[row][column] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            game_field = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(BLACK)

    if (query-1) % 2 == 0:
        game_over = check_win(game_field, 'x')
    else:
        game_over = check_win(game_field, 'o')

    if game_over:
        screen.fill(BLACK)
        font = pygame.font.SysFont('futura', 100)
        if check_win(game_field, 'o'):
            if game_over == "Draw!":
                screen.blit(font.render("Draw!", 1, GREEN), (415, 110))
            else:
                screen.blit(font.render("O win!", 1, GREEN), (415, 110))
        elif check_win(game_field, 'x'):
            screen.blit(font.render("X win!", 1, BLUE), (415, 110))

    for col in range(3):
        for row in range(3):
            if game_field[row][col] == 'x':
                color = BLUE
            elif game_field[row][col] == 'o':
                color = GREEN
            else:
                color = WHITE
            x = col * SIZE_BLOCK + (col+1) * MARGIN
            y = row * SIZE_BLOCK + (row+1) * MARGIN
            pygame.draw.rect(screen, color, (x, y, SIZE_BLOCK, SIZE_BLOCK))
            if color == BLUE:
                pygame.draw.line(screen, WHITE, (x + 25, y + 25), (x + SIZE_BLOCK - 25, y + SIZE_BLOCK - 25), 7)
                pygame.draw.line(screen, WHITE, (x + SIZE_BLOCK - 25, y + 25), (x + 25, y + SIZE_BLOCK - 25), 7)
            elif color == GREEN:
                pygame.draw.circle(screen, WHITE, (x + SIZE_BLOCK // 2, y + SIZE_BLOCK // 2), SIZE_BLOCK // 2 - 20, 5)

    pygame.display.update()
