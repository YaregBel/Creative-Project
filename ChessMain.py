"""
Главный файл загрузки.
"""

# Импортируем библиотеку pygame и наш скрипт ChessEngine
import pygame
import pygame.rect

from chess import ChessEngine

pygame.init()

WIDTH = HEIGHT = 800 # Ширина = Высоте = 800
DIMENSION = 8 # Размерность нашей доски 8x8 равна 8
SQ_SIZE = HEIGHT // DIMENSION # Размер квадрата
IMAGES = {}
MAX_FPS = 15

"""
Инициализируем словарь изображений фигур
"""
def loadImages():
    pieces = ["wP", "wK", "wN", "wR", "wQ", "wB", "wP", "bP", "bK", "bQ", "bB", "bN", "bR"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    pygame.init()   # pygame.init() - команда, запускающая pygame.
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for evnt in pygame.event.get():
            if evnt.type == pygame.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pygame.display.flip()

# Тут будет производится отрисовка доски с фигурами
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

# Рисуем квадраты на доске
def drawBoard(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Рисуем фигуры на доске
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()





