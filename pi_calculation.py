import random
import math
from statistics import mean, standard_deviation


def throw_needles(number_of_needles):
    inside_the_circle = 0

    for _ in range(number_of_needles):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distance_from_center = math.sqrt(x**2 + y**2)

        if distance_from_center <= 1:
            inside_the_circle += 1

    return (4 * inside_the_circle) / number_of_needles


def estimation(number_of_needles, number_of_tries):
    estimates = []

    for _ in range(number_of_tries):
        estimation_pi = throw_needles(number_of_needles)
        estimates.append(estimation_pi)
    
    estimated_mean = mean(estimates)
    sigma = standard_deviation(estimates)

    print(f'Estimates mean = {round(estimated_mean, 5)}, sigma or standard deviation = {round(sigma, 5)}, number of needles = {number_of_needles}')

    return (estimated_mean, sigma)


def estimate_pi(precision, number_of_tries):
    number_of_needles = 1000
    sigma = precision 

    while sigma >= precision / 1.96:
        mean, sigma = estimation(number_of_needles, number_of_tries)
        number_of_needles *= 2

    return mean


if __name__ == '__main__':
    estimate_pi(0.01, 1000)