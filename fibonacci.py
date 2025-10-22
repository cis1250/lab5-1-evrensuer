#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def valid(x):
    while True:
        try:
            test=int(x)
            if type(test) == int and test>=0:
                return x
                break
            else:
                x= input("Error, Try again ")
        except ValueError:
            x= input("Error, Try again ")
            
def generate(l):
    n1=0
    n2=1
    n=0
    for i in range(l):
        display(n1)
        n=n2
        n2=n1+n2
        n1=n
    
def display(n):
    print(n)
    
    
fib = input("Enter a positive intiger : ")
fib = valid(fib)
generate(int(fib))
