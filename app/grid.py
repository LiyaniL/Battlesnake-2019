import snakeinfo as si

# Create the grid to track the python
def createGrid(data):
    board = si.board(
        data['board']['height'], 
        data['board']['width'],
        data['board']['food'],
        data['board']['snakes'],
        data['board']['snakes'][0]
    )

    ourSnake = si.ourSnake(
        data['you']['id'],
        data['you']['name'],
        data['you']['health'],
        data['you']['body'],
        data['you']['body'][0]['x'],
        data['you']['body'][0]['y']
    )

    # Grid Position variable declaration
    head = 3
    snake = 4
    food = 1

    # Class variable declarations
    # Board
    width = board.width
    height = board.height
    foodPos = board.food
    allSnakes = board.snakes
    enemyHealth = board.health

    # for snakes in allSnakes:
    #     board.printHealth(snakes['name'], snakes['health'])

    #Our snake
    sid = ourSnake.sid
    name = ourSnake.name
    ourHealth = ourSnake.health
    ourBody = ourSnake.body
    ourX = ourSnake.x
    ourY = ourSnake.y
    



    grid = [[0 for col in range(width)] for row in range(height)]
    # Plotting out the food in the grid
    for eat in foodPos:
        grid[eat['y']][eat['x']] = food

    # Snakes placed in the grid 
    for snakes in allSnakes:
        x = snakes['body'][0]['x']
        y = snakes['body'][0]['y']
        grid[y][x] = head    

    for cords in snakes['body']:
        grid[cords['y']][cords['x']] = snake

    # Our snakes head and body positions
    grid[ourY][ourX] = head
    for cords in ourBody:
        grid[cords['y']][cords['x']] = snake

    return grid