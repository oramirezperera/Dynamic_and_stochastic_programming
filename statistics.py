import random
import math


def mean(X):
    return sum(X) / len(X)


def variance(X):
    mu = mean(X)

    acumulator = 0
    for x in X:
        acumulator += (x - mu)**2
    return acumulator / len(X)


def standard_deviation(X):
    return math.sqrt(variance(X))


if __name__ == '__main__':
    X = [random.randint(1, 20) for i in range(20)]
    mu = mean(X)

    print(X)
    print(mu)