#  Grid Creation for battlesnake

food = 1

## snakes start out with a default body size of 4 
head = 3
snake = 4

## Create a grid from the data given 
def createGrid(data):
    head = 3
    snake = 4
    food = 1

    grid = [[0 for col in range(data['width'])] for row in range(data['height'])]

    ## Plotting out the food in the grid
    for eat in data['food']:
        grid[eat['x']][eat['y']] = food

    ## Snakes placed in the grid 
    for snakes in data['snakes']:
        for cords in snakes['coords']:
            grid[cords[0]][cords[1]] = snake
            grid[snakes['coords'][0]][snakes['coords'][1]] = head
    return grid