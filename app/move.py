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
    return (tailX, tailY)

def findFood(board, x, y):
    foodToEat = (board.food[0]['x'],board.food[0]['y'])
    # print("food[x] = " + str(board.food[0]['x']))
    # print("x = " + str(x))
    # print("food[y] = " + str(board.food[0]['y']))
    # print("y = " + str(y))
    # print("plus x is " + str(board.food[0]['x'] + x))
    # print("plus y is " + str(board.food[0]['y'] + y))
    for food in board.food:
        if((abs(food['x'] - x) + abs(food['y'] - y)) < abs((foodToEat[0] - x) + abs(foodToEat[1] - y))):
            foodToEat = (food['x'], food['y'])
        # print(str(food['x']) + "iterating")
    return foodToEat
    

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
    if(len(board.food[0]) == 0):
        state = 3
    else:
        state = 1

    tailPoint = followTail(tailX, tailY)
    
 
    # print(ourHealth)
    # print(tailPoint[0], tailPoint[1])
    # if ourHealth >= 80:
        # state = 2

    # elif ourHealth == 100:
    # end = grid.node(tailPoint[0], tailPoint[1])


    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    if(state == 1):
        foodToEat = findFood(board, ourX, ourY)
        end = grid.node(foodToEat[0], foodToEat[1])
    elif(state == 2):
        end = grid.node(tailPoint[0], tailPoint[1])
    elif(state == 3):
        end = grid.node(0, 0)
    # else:
    #     end = grid.node(board.food[0]['x'], board.food[0]['y'])
    
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

    path, runs = finder.find_path(start, end, grid)
    next_path = path[1]
    # print(start)
    # print(next_path)
    # print(next_path[0], next_path[1])
    # print(start.x + 1)
    # print ('operations: ', runs, 'path length: ', len(path))
    # print(grid.grid_str(path=path, start=start, end=end))

    if (next_path[0] == start.x + 1):
        print ("Right?")
        return 3

    elif (next_path[0] == start.x - 1):
        print ("Left")
        return 2
    
    elif (next_path[1] == start.y + 1):
        print ("Up")
        return 1

    else:
        print ("Down")
        return 0

