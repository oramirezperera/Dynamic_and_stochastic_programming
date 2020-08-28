import random

def mean(X):
    return sum(X) / len(X)


if __name__ == '__main__':
    X = [random.randint(1, 20) for i in range(20)]
    mu = mean(X)

    print(X)
    print(mu)