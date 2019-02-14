import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

def createGrid(data):
    head = 3
    snake = 4
    food = 1

    grid = [[0 for col in range(data['board']['width'])] for row in range(data['board']['height'])]

    ## Plotting out the food in the grid
    for eat in data['board']['food']:
        grid[eat['x']][eat['y']] = food

    ## Snakes placed in the grid 
    for snakes in data['board']['snakes']:
         for cords in snakes['body']:
             grid[cords['x']][cords['y']] = snake
            #  grid[snakes['body']['x']][snakes[['body']['y']]] = head
    return grid


@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/head.png')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/head.png')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00FF00"

    return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json
    grid = createGrid(data)

    print (grid)
    # print(json.dumps(data))

    directions = ['up', 'down', 'left', 'right']

    direction = random.choice(directions)

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
