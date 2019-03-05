# This will deal with the movement of the snake
import snakeinfo as si
import getFood
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
directions = ['up', 'down', 'left', 'right']

def followTail(x, y):
    tailX = x
    tailY = y
    tailPoint = (tailX, tailY)
    return tailPoint

def checkHealth(health):
    if health >= 80:
        print("true")
        return True


def findFood(board, x, y):
    foodToEat = (board.food[0]['x'],board.food[0]['y'])
    for food in board.food:
        if((abs(food['x'] - x) + abs(food['y'] - y)) < abs((foodToEat[0] - x) + abs(foodToEat[1] - y))):
            foodToEat = (food['x'], food['y'])
    return foodToEat
    

def is_empty(any_structure):
    if any_structure:
        print('Structure is not empty.')
        return False
    else:
        print('Structure is empty.')
        return True

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

    # for snake in board.snakes:
    #     print(snake)
    # print(board.food)
    # print(data)
    sid = ourSnake.sid
    name = ourSnake.name
    ourHealth = ourSnake.health
    ourBody = ourSnake.body
    ourX = ourSnake.x
    ourY = ourSnake.y
    tailX = ourSnake.tailX
    tailY = ourSnake.tailY
    start = grid.node(ourX, ourY)

    if(len(board.food) == 0):
        state = 3
    print(ourBody)
    if (len(ourBody) > 10 and (ourHealth >= 50)):
        print("In Second State")
        state = 2
    else:
        state = 1

    tailPoint = followTail(tailX, tailY)
    # foodToEat[0], foodToEat[1]
   
    # print(tailPoint[1])
    # print(ourHealth)
    # if (checkHealth(ourHealth)):
    #     state = 2
    foodToEat = findFood(board, ourX, ourY)
    end = grid.node(foodToEat[0], foodToEat[1])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.only_when_no_obstacle)

    if(state == 1):
        print("state 1")
        foodToEat = findFood(board, ourX, ourY)
        print (tailPoint)
        end = grid.node(foodToEat[0], foodToEat[1])
        state = 2

    elif(state == 2):
        print("state 2")
        end = grid.node(tailPoint[0], tailPoint[1])

    elif(state == 3):
        print("state 3")
        end = grid.node(tailPoint[0], tailPoint[1])
    
    finder = AStarFinder(diagonal_movement=DiagonalMovement.only_when_no_obstacle)

    path, runs = finder.find_path(start, end, grid)
    print(path)
    next_path = path[1]          
    if (is_empty(next_path)):
        print("Invalid Move.... Remapping")
        end = grid.node(tailPoint[0], tailPoint[1])
        finder = AStarFinder(diagonal_movement=DiagonalMovement.only_when_no_obstacle)
        path, runs = finder.find_path(start, end, grid)

    # print(start)
    # print(next_path)
    # print(next_path[0], next_path[1])
    # print(start.x + 1)
    print ('operations: ', runs, 'path length: ', len(path))
    print(grid.grid_str(path=path, start=start, end=end))

    if (next_path[0] == start.x + 1):
        # print ("Right?")
        return 3

    elif (next_path[0] == start.x - 1):
        # print ("Left")
        return 2
    
    elif (next_path[1] == start.y + 1):
        # print ("Up")
        return 1

    else:
        # print ("Down")
        return 0

