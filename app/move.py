# This will deal with the movement of the snake
import snakeinfo as si
import getFood
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
directions = ['up', 'down', 'left', 'right']

def generatePath(grid, data):
    grid = Grid(matrix=grid)

    def getFood():
        
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
    print("food local = " + str(board.food[0]), + str(board.food[1]))
    start = grid.node(ourX, ourY)
    end = grid.node(0, 0)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

    path, runs = finder.find_path(start, end, grid)
    print(path[1])
    print ('operations: ', runs, 'path length: ', len(path))
    print(grid.grid_str(path=path, start=start, end=end))

    
