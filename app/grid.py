import snakeinfo as si

# Create the grid to track the python
def createGrid(data):
    board = si.board(
        data['board']['height'], 
        data['board']['width'],
        data['board']['food'],
        data['board']['snakes']
    )
    board.printFood()

    # Grid Position variable declaration
    head = 3
    snake = 4
    food = 1

    # Class variable declarations
    width = board.width
    height = board.height
    foodPos = board.food
    allSnakes = board.snakes

    

    grid = [[0 for col in range(width)] for row in range(height)]
    ## Plotting out the food in the grid
    for eat in foodPos:
        grid[eat['y']][eat['x']] = food

    ## Snakes placed in the grid 
    for snakes in allSnakes:
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