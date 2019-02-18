
# This function gets all the data from the json and sets them to variables for easy use 
class boardDimension:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board(self):
        print("Board is: ", self.height, " x ", self.width)


