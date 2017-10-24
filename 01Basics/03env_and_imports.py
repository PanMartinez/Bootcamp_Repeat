from random import randint

import requests

"""
Exercise 1
Make virtualenv catalog. Enter it, and activate.
Install 'requests' library, and write simple program, that will take html from any website.
"""


# Creating new virtualenv - virtualenv -p python3 env

# Instaling requests library in env - pip install requests


def get_html(url):
    r = requests.get(url)
    return r.text


print("1#", get_html("https://singlemalt.pl/"))

"""
Exercise 2
Write a 'random average" function that will get 'n' random numbers in range 1 - 100, sum them, and return average.
"""


def random_average(n):
    sum = 0
    num = 0
    for i in range(0, n):
        sum += randint(1, 100)
        num += 1
    return sum / num


print("2#", random_average(10))

"""
Exercise 3
Write program, that will ask user to write 2 numbers, divise those numbers, and print final result.
Also secure Your code from posible errors.
"""

def division_check():

    a = input("Enter number a: ")
    b = input("Enter number b: ")

    try:
        x = int(a)
        y = int(b)

    except ValueError:
        print("You need to put a number")

    except ZeroDivisionError:
        print("You can't divise by zero")

    return x / y


print("3#", division_check())


"""
Exercise 4
Write a function that will check validation of PESEL number. Function will take string as a value and return 
boolean value. PESEL contains 11 numbers. Last number is a control number. First 10 numbers should be multiple by
following numbers: `1 3 7 9 1 3 7 9 1 3`. Those numbers should be summed, then divided by 10 and finally minus
10. If number You get will be equal to control number PESEL number is correct.
"""
