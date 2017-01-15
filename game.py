
grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]


def winner():
    global grid, players

    win_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

    flat_grid = []
    for row in grid:
        for value in row:
            flat_grid.append(value)

    for player in players:
        for win_con in win_conditions:

            score = 0
            for index in win_con:

                if flat_grid[index] == player:
                    score += 1

            if score == 3:
                return player
            
    return None


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

            try:
                print()
                show_grid()
                coord_str = input("Where would you like to place your marker player '" + player + "'? ")
                coords = list(eval(coord_str))

                coords[0] -= 1
                coords[1] -= 1

                if coords[0] > 2 or coords[0] < 0 or coords[1] > 2 or coords[1] < 0:
                    print('Values between 1 and 3 please')

                elif try_move(coords, player):
                    break
                
                else:
                    print('That spot is taken up, try a different one')
                    
            except:
                print('Coordinates please (in the form (x,y) or x,y)')
        
            

        











        
