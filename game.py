
grid = [
    [None, None, None],
    ['o', 'x', None],
    [None, None, 'x']
    ]


def show_grid(grid):

    for row_index in range(3):
        row = grid[row_index]

        for value_index in range(3):
            value = row[value_index]

            if value == None:
                print('.', end = ' ')
            else:
                print(value, end = ' ')

        print()


show_grid(grid)
