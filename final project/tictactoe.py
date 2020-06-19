"""
File: FinalProject.py
-----------------------
It's just a simple TicTacToe :)
"""
import tkinter

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Tic-Tac-Toe')
    while game(canvas) is True:
        canvas.mainloop()


def game(canvas):
    """
    Here's where the whole Game
    Algorithm is working.
    """
    draw_game_lines(canvas)  # Draw the game structure on Canvas
    label_grid(canvas)  # Put one number, from 1-9, for each grid on canvas

    x_list = []  # List of X's on the grid
    o_list = []  # List O's on the grid
    occupied_grid = []  # List of all o User Inputs
    player_count = 1

    while True:
        user = int(input(f"Player {player_count}: "))
        user = check_square(user, player_count, occupied_grid)
        while user < 1 or user > 9:
            user = int(input(f"Player {player_count}, Enter a num from 1-9: "))
            user = check_square(user, player_count, occupied_grid)
        # Draw 'X' or 'O' at UI location
        if player_count == 1:
            draw_xs(canvas, user)
            x_list.append(user)
        else:
            draw_circles(canvas, user)
            o_list.append(user)
        # Check if has, or not, a Winner
        if check_winner(x_list, o_list, occupied_grid) is True:
            break
        # Update the Player counting
        player_count = update_player(player_count)


def check_winner(x_list, o_list, occupied_grid):
    if compare_lists(x_list, o_list) is True:
        return True
    # Makes the game stop after all grids are taken
    if len(occupied_grid) == 9:
        print("We have a tie!")
        return True


def compare_lists(x_list, o_list):
    """
    Checks if the Player 1 or Player 2 won the game.
    It checks by comparing the items on the list of X's
    and the list of O's with the Xablau list, which contains
    lists TicTacToe Win Patterns.
    """
    xablau = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
              [1, 4, 7], [2, 5, 8], [3, 6, 9],
              [1, 5, 9], [3, 5, 7]]

    for i in range(8):
        check = all(item in x_list for item in xablau[i])
        if check is True:
            print(f"Player 1 Won!")
            return True
        check = all(item in o_list for item in xablau[i])
        if check is True:
            print("Player 2 Won!")
            return True


def check_square(user, player_count, occupied_grid):
    while user in occupied_grid:
        print(f"Occupied Squares: {occupied_grid}")
        print("")
        user = int(input(f"Player {player_count}, Enter a clear space: "))

    if (user >= 1) and (user <= 9):
        occupied_grid.append(user)
        occupied_grid.sort()
    return user


def update_player(player_count):
    """
    Update the player countage
    """
    if player_count == 1:
        player_count += 1
    else:
        player_count -= 1
    return player_count


def draw_game_lines(canvas):
    """
    Draws the Horizontal and Vertical lines,
    making a '#' on Canvas.
    """
    # Horizontal Lines
    canvas.create_line(0, 199, CANVAS_WIDTH, 199)
    canvas.create_line(0, 398, CANVAS_WIDTH, 398)

    # Vertical Lines
    canvas.create_line(199, 0, 199, CANVAS_HEIGHT)
    canvas.create_line(398, 0, 398, CANVAS_HEIGHT)


def label_grid(canvas):
    """
    Label a number, from 1-9, for
    each grid on Canvas.
    """
    canvas.create_text(95, 10, anchor='w', font='Times', text='1')
    canvas.create_text(295, 10, anchor='w', font='Times', text='2')
    canvas.create_text(495, 10, anchor='w', font='Times', text='3')
    canvas.create_text(95, 209, anchor='w', font='Times', text='4')
    canvas.create_text(295, 209, anchor='w', font='Times', text='5')
    canvas.create_text(495, 209, anchor='w', font='Times', text='6')
    canvas.create_text(95, 408, anchor='w', font='Times', text='7')
    canvas.create_text(295, 408, anchor='w', font='Times', text='8')
    canvas.create_text(495, 408, anchor='w', font='Times', text='9')


def draw_circles(canvas, user):
    """
    Creates lines which draws 'X's
    according user input.
    """
    if user == 1:  # [0,0] square
        canvas.create_oval(0, 0, 199, 199)

    elif user == 2:  # [0,1] square
        canvas.create_oval(199, 0, 398, 199)

    elif user == 3:  # [0,2] square
        canvas.create_oval(398, 0, 600, 199)

    elif user == 4:  # [1,0] square
        canvas.create_oval(0, 199, 199, 398)

    elif user == 5:  # [1,1] square
        canvas.create_oval(199, 199, 398, 398)

    elif user == 6:  # [1,2] square
        canvas.create_oval(398, 199, 600, 398)

    elif user == 7:  # [2,0] square
        canvas.create_oval(0, 398, 199, 600)

    elif user == 8:  # [2,1] square
        canvas.create_oval(199, 398, 398, 600)

    elif user == 9:  # [2,2] square
        canvas.create_oval(398, 398, 600, 600)


def draw_xs(canvas, user):
    """
    Creates lines which draws 'X's
    according user input.
    """
    if user == 1:  # [0,0] square
        canvas.create_line(0, 0, 199, 199)
        canvas.create_line(0, 199, 199, 0)

    elif user == 2:  # [0,1] square
        canvas.create_line(199, 0, 398, 199)
        canvas.create_line(199, 199, 398, 0)

    elif user == 3:  # [0,2] square
        canvas.create_line(398, 0, 600, 199)
        canvas.create_line(398, 199, 600, 0)

    elif user == 4:  # [1,0] square
        canvas.create_line(0, 199, 199, 398)
        canvas.create_line(0, 398, 199, 199)

    elif user == 5:  # [1,1] square
        canvas.create_line(199, 199, 398, 398)
        canvas.create_line(199, 398, 398, 199)

    elif user == 6:  # [1,2] square
        canvas.create_line(398, 199, 600, 398)
        canvas.create_line(398, 398, 600, 199)

    elif user == 7:  # [2,0] square
        canvas.create_line(0, 398, 199, 600)
        canvas.create_line(0, 600, 199, 398)

    elif user == 8:  # [2,1] square
        canvas.create_line(199, 398, 398, 600)
        canvas.create_line(199, 600, 398, 398)

    elif user == 9:  # [2,2] square
        canvas.create_line(398, 398, 600, 600)
        canvas.create_line(398, 600, 600, 398)


def make_canvas(width, height, title=None):
    """
    Creates and returns a drawing canvas
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
