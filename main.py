import pygame
import time
from GUI import Board, redraw_window

pygame.font.init()

def main():
    win = pygame.display.set_mode((540,600))  
    pygame.display.set_caption("Sudoku")
    board = Board(540, 540, win)  # dimensions of the board
    key = None
    run = True
    start = time.time()
    strikes = 0  # wrong sign 'X' for rong answers
    
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                    
                if event.key == pygame.K_SPACE:
                    board.auto_solve()
                    
                if event.key == pygame.k_ESC:
                    pygame.time.delay(500)
                    pygame.quit()
                    
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cells[i][j].temp != 0:
                        if board.place(board.cells[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1  # wrong sign 'X'
                        key = None

                        if board.is_finished():
                            print("Game over")
                            run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()