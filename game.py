
grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]


def show_grid():
    global grid

    for row_index in range(3):
        row = grid[row_index]

        for value_index in range(3):
            value = row[value_index]

            if value == None:
                print('.', end = ' ')
            else:
                print(value, end = ' ')
        print()


def try_move(pos, player):
    global grid
    value = grid[pos[1]][pos[0]]

    if value == None:
        grid[pos[1]][pos[0]] = player
        return True
    return False


players = ['x', 'o']

# Game loop
while True:

    for player in players:

        while True:
            print()
            show_grid()
            coord_str = input("Where would you like to place your marker player '" + player + "'? ")
            coords = eval(coord_str)
        
            if try_move(coords, player):
                break
            else:
                print('That spot is taken up, try a different one')

        











        
