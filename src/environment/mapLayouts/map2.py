def generate():

    layout = [
    "#                                #",
    "#                                #",
    "#            ########            #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#     ######          ######     #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#                                #",
    "#            ########            #",
    "#                                #",
    "#                                #"
    ]

    grid = []

    for row in layout:

        grid_row = []

        for char in row:
            if char == "#":
                grid_row.append(3)
            else:
                grid_row.append(0)
        
        grid.append(grid_row)

    return grid