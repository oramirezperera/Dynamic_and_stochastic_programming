# This program is good for small fibonacci but for big like 50 it's not so good.
def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

if __name__ == '__main__':
    n = int(input('Please, write a number: '))

    result = recursive_fibonacci(n)
    print(result)
