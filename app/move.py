# This will deal with the movement of the snake
import snakeinfo as si
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
directions = ['up', 'down', 'left', 'right']

def followTail(health, x, y):
    tailX = x
    tailY = y
    if health == 100:
        return (tailX, tailY)

# def findFood(board):
#     return (board.food[0]['x'],board.food[0]['y'])
    

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
        data['you']['body'][0]['y'],
        data['you']['body'][-1]['x'],
        data['you']['body'][-1]['y']
    )

    sid = ourSnake.sid
    name = ourSnake.name
    ourHealth = ourSnake.health
    ourBody = ourSnake.body
    ourX = ourSnake.x
    ourY = ourSnake.y
    tailX = ourSnake.tailX
    tailY = ourSnake.tailY
    state = 1
    start = grid.node(ourX, ourY)


    # if(state == 1):
    #     end = grid.node(findFood(board))
    tailPoint = followTail(ourHealth, tailX, tailY)
    
    end = grid.node(0, 0)
    print(ourHealth)
    if ourHealth != 100:
        print("checking health") 
        end = grid.node(board.food[0]['x'],board.food[0]['y'])
    # elif ourHealth == 100:
    # end = grid.node(tailPoint[0], tailPoint[1])


    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    next_path = path[1]
    print(start)
    # print(next_path)
    print(next_path[0], next_path[1])
    print(start.x + 1)

    if (next_path[0] == start.x + 1):
        print ("Right?")
        return 3

    if (next_path[0] == start.x - 1):
        print ("Left")
        return 2
    
    if (next_path[1] == start.y + 1):
        print ("Up")
        return 1

    if (next_path[1] == start.y - 1):
        print ("Down")
        return 0
    # print ('operations: ', runs, 'path length: ', len(path))
    print(grid.grid_str(path=path, start=start, end=end))

