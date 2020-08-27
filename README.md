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
        - [External links for random walk](#External-links-for-random-walk)
    2. [Class 5 Drunkard's Walk](#Class-5-Drunkard's-Walk)
4. [Fourth Module Stochastic Programs](#Fourth-Module-Stochastic-Programs)
    1. [Class 8 Introduction to Stochastic Programming](#Class-8-Introduction-to-Stochastic-Programming)
        - [Deterministic vs Stochastic programming](#Deterministic-vs-Stochastic-programming)
        - [Examples](#Examples)
    2. [Class 9 Probabilities calculation](#Class-9-Probabilities-calculation)
        - [Probabilities](#Probabilities)


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

### External links for Random Walk

[PBS infinite series]([https://www.youtube.com/watch?v=stgYW6M5o4k](https://www.youtube.com/watch?v=stgYW6M5o4k))

[Socratica]([https://www.youtube.com/watch?v=BfS2H1y6tzQ](https://www.youtube.com/watch?v=BfS2H1y6tzQ))

### Class 5 drunkard's walk

is an algorithm for a simulation.

starts at (0,0) in a Cartesian plane where you can move right, left, up, and down with the same probability (25%).

We can generate a Hypothesis, What happens after 10 steps? Are we close or are we far? what happens after 100, 1000, 10000 steps? What happens if we do it in 3 dimensions or 4. What happens if the distribution of probability is not the same?

You can calculate the final distance with the Pythagoras theorem.

the idea of this program is generate three classes.

1. class drunkard named drunk.

2. class abstraction of coordinates called coordinate.

3. class Cartesian plane called field (only in a field you can walk like this haha).

I did all the three classes and made all the program, now if you run it, you can see how far your drunkard\'s has gone.

There are two classes of drunkard\'s Traditional drunkard\'s who is aleatory and Fallen drunkard\'s who is trying to go up in a hill.

## Fourth Module Stochastic Programs

### Class 8 Introduction to Stochastic programming

#### Deterministic vs Stochastic programming

- A program is deterministic when if you use the same input you get the same output.
- Deterministic programming is very important but not all problems can be solved with this method.
- Stochastic programming lets us to introduce randomness to our programs, so we can create simulation for solving different problems.
- Stochastic programs use as advantage that a problem can have probabilistic distribution or it can be estimated.

#### Examples 

1. Traffic handling.
2. Fleet schedule.
3. Physics simulations.
4. Financial simulations.
5. Drugs and medicine effects simulations.
6. Self-driving car development.

Stochastic programming uses probabilistic distributions that could be pre-defined or estimated via statistical inference.

Another example could be understanding the pattern of use of a traffic light intersection so you can choose better when will be red or green the traffic light.

The way that we see the problem is important because that affects the solution that we will give it.

We have to know the population.

### Class 9 Probabilities calculation

#### Probabilities

- Probabilities are a measure of how likely is an event to occur in the future and the probability of an event is a number between 0 and 1.
- A probability of 0 indicates an impossibility of the event.
- A probability of 1 indicates a certainty.
- When we use probability we ask what fraction of all of the possible events has the properties that we are looking for.
- Because of that is important to calculate all the possibilities that has an event, so we can understand their probability.
- The probability of an event to occur or not is 1
- P(A) + P(notA) = 1. Compliment law.
- P(A and B) =  P(A) * P(B). Only if the two events are independent. Multiplication law. It always be less than the probability of only one of those.
- P(A or B) = P(A) + P(B). If they are mutually exclusive events.
- P(A or B) = P(A) + P(B)  - P(A and B). If the are not mutually exclusive events. Addition law.