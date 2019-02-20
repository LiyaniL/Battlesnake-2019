
# These classes get all the data from the json and sets them to variables for easy use 

# This class deals with the board including all snakes and food
class board:
    def __init__(self, height, width, food, snakes):
        self.height = height
        self.width = width
        self.food = food
        self.snakes = snakes


    def printBoard(self):
        print("Board is: ", self.height, " x ", self.width)

    def printFood(self):
        print("Food is at position(s): ", self.food)

# This class deals with the heads of all snakes in the board
class sHead:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printHead(self):
        print("Head is at: ", self.x, " : ", self.y)


# This class deals with our snakes id, name, health, and body position
class ourSnake:
    def __init__(self, sid, name, health, x, y):
        self.sid = sid
        self.name = name
        self.health = health
        self.x = x
        self.y = y
    
    def printHead(self):
        print("Head is at: ", self.x, " : ", self.y)