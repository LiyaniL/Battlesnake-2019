# This will deal with the movement of the snake
import snakeinfo as si
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
directions = ['up', 'down', 'left', 'right']
def generatePath(grid, data):
    grid = Grid(matrix=grid)

    # Board class declaration
    board = si.board (
        data['board']['height'], 
        data['board']['width'],
        data['board']['food'],
        data['board']['snakes'],
        data['board']['snakes'][0]
    )

    width = board.width
    height = board.height
    foodPos = board.food
    allSnakes = board.snakes
    enemyHealth = board.health

    # Our snakes class declaration
    ourSnake = si.ourSnake (
        data['you']['id'],
        data['you']['name'],
        data['you']['health'],
        data['you']['body'],
        data['you']['body'][0]['x'],
        data['you']['body'][0]['y']
    )

    sid = ourSnake.sid
    name = ourSnake.name
    ourHealth = ourSnake.health
    ourBody = ourSnake.body
    ourX = ourSnake.x
    ourY = ourSnake.y

    start = grid.node(ourX, ourY)
    end = grid.node(0, 0)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    next_path = path
    print(start)
    print(next_path)
    print(grid.node(ourX, ourY))
    if (next_path == grid.node(ourX + 1, ourY)):
        print ("Right?")
        return 3
    
    elif (next_path == grid.node(ourX - 1, ourY)):
        print ("Left?")
        return 2

    if (next_path == grid.node(ourX, ourY + 1)):
        print ("Down?")
        return 1

    if (next_path == grid.node(ourX, ourY - 1)):
        print ("Up?")
        return 0

    else:
        return 1
    # print ('operations: ', runs, 'path length: ', len(path))
    # print(grid.grid_str(path=path, start=start, end=end))

