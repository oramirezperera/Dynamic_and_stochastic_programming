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

## First Module Introduction

### class 1 course objectives

- Learn when to use Dynamic programming and it's benefits.

- Understand the difference between stochastic and deterministic programming.

- Learn to use stochastic programming.

- Learn to create valid computational simulations.

## Second Module Dynamic Programming

### class 2 Introduction to Dynamic Programming

#### Richard Bellman

![Richard Bellman](https://en.wikipedia.org/wiki/Richard_E._Bellman#/media/File:Richard_Ernest_Bellman.jpg)

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