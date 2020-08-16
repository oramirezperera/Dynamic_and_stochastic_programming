class Field:
    
    def __init__(self):
        self.coordinate_of_drunk = {} # creates a dictionary where it's the coordinates of the drunkards

    def add_drunk(self, drunk, coordinate):
        self.coordinate_of_drunk[drunk] = coordinate #adds the coordinate as a value in the dictionary
    
    def move_drunk(self, drunk):

        delta_x, delta_y = drunk.walk()
        actual_coordinate = self.coordinate_of_drunk[drunk]
        new_coodinate = actual_coordinate.move(delta_x, delta_y)

        self.coordinate_of_drunk[drunk] = new_coodinate

    def get_coordinate(self, drunk):
        return self.coordinate_of_drunk[drunk]