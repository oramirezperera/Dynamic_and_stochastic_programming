# Dynamic_and_stochastic_programming
Notes and programs from Platzi\'s Dynamic and stochastic programming with Python course

## Index
[TOCM]

[TOC]

1. [First Module Introduction](#First-Module-Introduction)
    1. [class 1 course objectives](#class-1-course-objectives)
2. [Second Module Dynamic Programming](#Second-Module-Dynamic-Programming)
    1. [Class 2 Introduction to Dynamic programming](#class-2-Introduction-to-Dynamic-Programming)
        - [Richard Bellman](#Richard-Bellman)
        - [Memoization](#Memoization)
    2. [Class 3 Fibonacci numbers](#Class-3-Fibonacci-numbers)
3. [Third Module Random Walk](#Third-Module-Random-Walk)
    1. [Class 4 What is Random Walk?](#Class-4-What-is-Random-Walk?)
        - [Brownian Motion](#Brownian-motion)
        - [Quantum Cloud Sculpture](#Quantum-Cloud-Sculpture)
## First Module Introduction

### class 1 course objectives

- Learn when to use Dynamic programming and it's benefits.

- Understand the difference between stochastic and deterministic programming.

- Learn to use stochastic programming.

- Learn to create valid computational simulations.

## Second Module Dynamic Programming

### class 2 Introduction to Dynamic Programming

#### Richard Bellman

![Richard Bellman](https://upload.wikimedia.org/wikipedia/en/7/7a/Richard_Ernest_Bellman.jpg)

> Richard Bellman introduced Dynamic Programming

Born in 1920 and died in 1984.

- Won the John Von Neumann Theory Prize in 1976.

- Studied mathematics at the Brooklyn College in 1941.

- He studied at the University of Wisconsin.

- Introduced Dynamic programming in the 1950s

> "The name 'Dynamic programming' was chosen to hide from governmental sponsors 'the fact that I was really doing mathematics... \[the phrase dynamic programming] was something not even a Congressman could object to.'" [Introduction to Computation and Programming Using Python, With application to Understanding Data - John V. Guttag](https://books.google.co.ve/books?id=KabKDAAAQBAJ&pg=PA203&lpg=PA203&dq=dynamic+programming+was+chosen+to+hide+the+sponsors&source=bl&ots=ETFSJ1L4dr&sig=ACfU3U0f_Cr-UkOz6GMB5aiAl24lS_4BdQ&hl=es-419&sa=X&ved=2ahUKEwiL493bpZPrAhXPzVkKHZN5AuIQ6AEwBHoECAkQAQ#v=onepage&q=dynamic%20programming%20was%20chosen%20to%20hide%20the%20sponsors&f=false)

Dynamic Programming == Mathematics

- Optimal Substructure: A global optimal solution can be found using local optimal sub-problems.

- Spliced problems: An optimal solution that can solve the same problem in different occasions.

#### Memoization

- Memoization is a technique to save previous results so you don't have to do it again.

- Normally is used with a dictionary, the queries can be made in O(1).
- Changes time for memory space (It's faster but consumes more memory)

### Class 3 Fibonacci numbers
Can be defined by:

$$ F_n = F_{n-1} + F_{n-2}$$

This is a recursive formula, it's easy to implement in code but it's very inefficient.

The calculation repeats itself more than once.

It's exponential O. 

So how can we optimize this implementation, first we use the recursive implementation and adding memoization. This approach has to be much better than only recursive.

In the dynamic implementation, I used a try, except flow control.
In the dynamic programming, file added the dictionary where you store the previous calculations. Now you can do really big calculations of Fibonacci numbers.

> note
 Python has a limit for recursion. The error is maximum recursion depth.

So if you want to avoid this error, I imported the sys module, and setting a new recursion limit.

## Third Module Random Walk

### class 4 What is random walk?

- It is a kind of simulation that takes a random decision in a set of valid decisions.
- it is used in a lot of fields of knowledge, when the deterministic decision aren't valid, and you need randomness.

#### Brownian motion

When the microscopic where invented, people saw that the particles moves were random. 

Einstein saw that the pollen motion was made by the individual water molecules, and modeled the motion.

the atomic motion is random.

You can't model this kind of motion in deterministic programming.

Not only at the microscopic level works the random walk.

The smoke can be simulated by this.

The merge of two galaxies can be simulated, using the gravity, and the behavior of each star and other inputs can model possibles outputs.

Our galaxy the Milky Way is on track to collide and merge with Andromeda.

Scientists are making models using random walk to simulate what can be the final result when this happens.

Not only in physics is used the random walk. In market simulations is used too.

#### Quantum Cloud Sculpture

There is a sculpture called Quantum Cloud Sculpture, is located in London, and is next to the O2 (an entertainment district in Greenwich at the southeast of London).

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Antony_Gormley_Quantum_Cloud_2000.jpg/457px-Antony_Gormley_Quantum_Cloud_2000.jpg)

