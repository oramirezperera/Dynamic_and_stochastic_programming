from drunk_walk import TraditionalDrunk # From drunk_walk file imports the TraditionalDrunk class
from drunk_walk import FallenDrunk
from field import Field
from coordinates import Coordinate # From the coordinates file imports the Coordinate class
from bokeh.plotting import figure, show, output_file, save


def walk(field, drunk, steps):
    start = field.get_coordinate(drunk)

    path_x = []
    path_y = []

    path_x.append(start.x)
    path_y.append(start.y)

    for i in range(steps):
        x_act = path_x[i]
        y_act = path_y[i]

        field.move_drunk(drunk)
        p = field.get_coordinate(drunk)

        path_x.append(p.x)
        path_y.append(p.y)

    plot_path(path_x, path_y)



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

def plotting(x, y):
    plot = figure(title='Drunkard\'s walk', x_axis_label='steps', y_axis_label='distance')
    plot.line(x, y, legend_label='mean distance')
    output_file('test.html')
    save(plot)

def plot_path(path_x, path_y):

    plot = figure(title='Drunkard\'s walk')
    plot.line(path_x, path_y)
    output_file('test.html')
    save(plot)

def main(walk_distances, number_of_tries, kind_of_drunk):
    mean_distances_walk = []
    for steps in walk_distances:
        distances = simulate_walk(steps, number_of_tries, kind_of_drunk)
        mean_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        mean_distances_walk.append(mean_distance)
        print(f'{kind_of_drunk.__name__} walked randomly {steps} steps')# .__name__ gives us the name of the class of this kind of drunk
        print(f'the mean distance was {mean_distance}')
        print(f'the max distance was {max_distance}')
        print(f'the minimum distance was {min_distance}')




if __name__ == '__main__': # The entry point of the program
    walk_distances = [10, 100, 1000, 10000] # number of steps
    number_of_tries = 100 # how many times the simulation will run

    # main(walk_distances, number_of_tries, FallenDrunk)
    
    main(walk_distances, number_of_tries, TraditionalDrunk)

