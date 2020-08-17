from drunk_walk import TraditionalDrunk # From drunk_walk file imports the TraditionalDrunk class
from field import Field # From the field file imports the Field class
from coordinates import Coordinate # From the coordinates file imports the Coordinate class


def walk(field, drunk, steps):
    start = field.get_coordinate(drunk)

    for _ in range(steps):
        field.move_drunk(drunk)

    return start.distance(field.get_coordinate(drunk))


def simulate_walk(steps, number_of_tries, kind_of_drunk):
    drunk = kind_of_drunk(name='Gragas') #this function doesn't depends on the type, this function knows that it needs a kind of drunk
    origin = Coordinate(0, 0)
    distances = []

    for _ in range(number_of_tries):  # the _ is used when you are not going to use this variable
        field = Field() #generates the field
        field.add_drunk(drunk, origin) #adds the drunkard and origin from the function add_drunk from the file field
        simulate_walk = walk(field, drunk, steps) #this uses a auxiliar function
        distances.append(round(simulate_walk, 1)) 
        
    return distances

def main(walk_distances, number_of_tries, kind_of_drunk):

    for steps in walk_distances:
        distances = simulate_walk(steps, number_of_tries, kind_of_drunk)
        mean_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        print(f'{kind_of_drunk:__name__} walked randomly {steps} steps')# .__name__ gives us the name of the class of this kind of drunk
        print(f'the mean distance was {mean_distance}')
        print(f'the max distance was {max_distance}')
        print(f'the minimum distance was {min_distance}')


if __name__ == '__main__': # The entry point of the program
    walk_distances = [10, 100, 1000, 10000] # number of steps
    number_of_tries = 100 # how many times the simulation will run

    main(walk_distances, number_of_tries, TraditionalDrunk)

