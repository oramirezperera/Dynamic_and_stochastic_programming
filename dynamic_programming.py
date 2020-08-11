import sys


# This approach is good for small fibonacci but for big like 50 it's not so good.
def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def dynamic_fibonacci(n, memo = {}): # here occurs the memoization the dictionary where you store the results
    if n == 0 or n == 1:
        return 1

    try: #used to pass if we don't have the n key
        return memo[n]
    except KeyError: # pass the step of not having the key to enter a certain dictionary
        result = dynamic_fibonacci(n - 1, memo) + dynamic_fibonacci(n - 2, memo)
        memo[n] = result #stores the result in the dictionary
    #using the try except to control the flow is a good practice, you are saying sorry and not permission
    # Tries to enter the value, and if the value doesn't exist, we put it in the try except and the code continues
        return result
    

if __name__ == '__main__':
    sys.setrecursionlimit(10000) #changed the recursion limit to calculate bigger numbers
    n = int(input('Please, write a number: '))
    result = dynamic_fibonacci(n)
    print(result)
