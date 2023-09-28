import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_COLOR = (0, 0, 0)
GRID_SIZE = 3
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Membuat layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tik Tak Tok")

# Inisialisasi papan permainan
grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Fungsi untuk menggambar papan permainan
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * GRID_HEIGHT), (SCREEN_WIDTH, row * GRID_HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (row * GRID_WIDTH, 0), (row * GRID_WIDTH, SCREEN_HEIGHT), 2)

def draw_markers():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            marker = grid[row][col]
            if marker == 'X':
                x_pos = col * GRID_WIDTH + GRID_WIDTH // 2
                y_pos = row * GRID_HEIGHT + GRID_HEIGHT // 2
                pygame.draw.line(screen, LINE_COLOR, (x_pos - 30, y_pos - 30), (x_pos + 30, y_pos + 30), 2)
                pygame.draw.line(screen, LINE_COLOR, (x_pos + 30, y_pos - 30), (x_pos - 30, y_pos + 30), 2)
            elif marker == 'O':
                x_pos = col * GRID_WIDTH + GRID_WIDTH // 2
                y_pos = row * GRID_HEIGHT + GRID_HEIGHT // 2
                pygame.draw.circle(screen, LINE_COLOR, (x_pos, y_pos), 30, 2)

def check_win(marker):
    # Periksa baris
    for row in range(GRID_SIZE):
        if all([grid[row][col] == marker for col in range(GRID_SIZE)]):
            return True

    # Periksa kolom
    for col in range(GRID_SIZE):
        if all([grid[row][col] == marker for row in range(GRID_SIZE)]):
            return True

    # Periksa diagonal utama
    if all([grid[i][i] == marker for i in range(GRID_SIZE)]):
        return True

    # Periksa diagonal kedua
    if all([grid[i][GRID_SIZE - 1 - i] == marker for i in range(GRID_SIZE)]):
        return True

    return False

# Loop permainan
player_turn = 'X'
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            col = x // GRID_WIDTH
            row = y // GRID_HEIGHT

            if grid[row][col] == ' ':
                grid[row][col] = player_turn

                if check_win(player_turn):
                    game_over = True
                else:
                    player_turn = 'O' if player_turn == 'X' else 'X'

    screen.fill((255, 255, 255))
    draw_grid()
    draw_markers()
    pygame.display.update()

# Menunggu sebelum keluar
pygame.time.wait(2000)
pygame.quit()
sys.exit()
