# This will deal with the movement of the snake
import snakeinfo as si

def moveSnake(data, direction):
    dirt = ['up', 'down', 'left', 'right']

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