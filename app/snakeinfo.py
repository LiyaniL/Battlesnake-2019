
# These classes get all the data from the json and sets them to variables for easy use 

# This class deals with the board including all snakes and food
class board:
    def __init__(self, height, width, food, snakes, health):
        self.height = height
        self.width = width
        self.food = food
        self.snakes = snakes
        self.health = health

    # prints the boards dimensions
    def printBoard(self):
        print("Board is: ", self.height, " x ", self.width)
    # prints the food on the board
    def printFood(self):
        print("Food is at position(s): ", self.food)
    # prints the health of each snake on the board
    def printHealth(self, name, health):
        print("Health of \"", name, "\" is: ", health)


# This class deals with our snakes id, name, health, and body position
class ourSnake:
    def __init__(self, sid, name, health, body, x, y, tailX, tailY):
        self.sid = sid
        self.name = name
        self.health = health
        self.body = body
        self.x = x
        self.y = y
        self.tailX = tailX
        self.tailY = tailY


    def printHead(self):
        print("Head is at: ", self.x, " : ", self.y)