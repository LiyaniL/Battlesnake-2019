import snakeinfo as si

# Create the grid to track the python
def createGrid(data):
    board = si.boardDimension(data['board']['height'], data['board']['width'])
    #board.board()
    head = 3
    snake = 4
    food = 1
    width = (board.width)
    #print(width)
    height = (board.height)
    #print(height)

    grid = [[0 for col in range(width)] for row in range(height)]
    ## Plotting out the food in the grid
    for eat in data['board']['food']:
        grid[eat['y']][eat['x']] = food

    ## Snakes placed in the grid 
    for snakes in data['board']['snakes']:
        x = snakes['body'][0]['x']
        y = snakes['body'][0]['y']
        grid[y][x] = head    
         
        for cords in snakes['body']:
            grid[cords['y']][cords['x']] = snake
            #  print("Head is at:", cords['y'])
            #  print("Head is at: ", cords['x'])
            # print("<======================>")
            #  grid[snakes['body']['x']][snakes[['body']['y']]] = head
    return grid