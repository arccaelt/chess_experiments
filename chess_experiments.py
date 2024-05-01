import chess
import pygame
from chess import pgn
    
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400
TILE_WIDTH = SCREEN_WIDTH // 8
TILE_HEIGHT = SCREEN_HEIGHT // 8

pygame.init()
display = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
running = True

game_file = open("game.pgn", "r")

game = pgn.read_game(game_file)
board = game.board()

def get_board_colors(board):
    colors = []
    row = []
    for square in chess.SQUARES:
        color = board.color_at(square)
        if color is not None:
            row.append("white" if color else "black")
        else:
            row.append("gray")
        if len(row) % 8 == 0:
            colors.append(row)
            row = []
    return colors


board_colors = get_board_colors(board)
print(board_colors)
moves = game.mainline_moves()
move_index = 0
moves_list = list(moves)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if move_index >= len(moves_list):
                    pass
                else:
                    next_move = moves_list[move_index]
                    move_index += 1
                    board.push(next_move)

                    for legal_move in board.legal_moves:
                        print(legal_move)
                        if board.is_legal(legal_move):
                             board.push(legal_move)

                    board_colors = get_board_colors(board)

    # draw the board
    for x in range(8):
        for y in range(8):
            pygame.draw.rect(display, board_colors[x][y],
                             (y * TILE_WIDTH, x * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
    pygame.display.flip()

pygame.quit()
