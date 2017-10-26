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


#print("1#", get_html("https://singlemalt.pl/"))

"""
Exercise 2
Write a function that take: random list, and the index, as a number. Function should return list element named "index".
If there is nothing like index, function should return None.
"""

def get_index(list, index):
    try:
        return list[index]

    except IndexError:

        return None

list = ["Rick", "Morty", "Summer", "Beth", "Jerry"]
print("2#", get_index(list, 0))
print("2#", get_index(list, 5))
print("2#", get_index(list, 1))
print("2#", get_index(list, 9))

"""
Exercise 3
Write a divide function that will take arguments a and b. Function should check if arguments are numbers, and take
care of zero divide error. Function should return result of division.
"""
def safe_division(a,b):

    try:
        return a/b
    except ZeroDivisionError:
        return None
    except IndexError:
        return

print("3#", safe_division(10,2))



"""
Exercise 4
Write function that will take phone number. Function should check if number is on your list number (make one). If not
Function should return exception with "no such number" comment.
"""

def phone_number(number):
    phone_list = [774896355, 990825630, 510836492, 276941862, 973245816]

    if number not in phone_list:
       raise Exception ("No such number on the list")

    return "Cellar No"

print("4#", phone_number(990825630))

"""
Exercise 5
There You have some simple riddle. Computer takes a random number between 1 and 10, and You have to guess it.
Analise code, and add exception methods.
"""

guessed = False
rnd = randint(1, 10)

while not guessed:
    str_num = input("Give me Your number:")

    try:
        num = int(str_num)
    except ValueError:
        print("Number please!")
        continue

    if num not in range(1, 11):
        print("number is between 1 and 10")

    if num == rnd:
        print("You got it!")
        guessed = True
    else:
        print("Try again")



"""
Exercise 6
Write a 'random average" function that will get 'n' random numbers in range 1 - 100, sum them, and return average.
"""


def random_average(n):
    sum = 0
    num = 0
    for i in range(0, n):
        sum += randint(1, 100)
        num += 1
    return sum / num


#print("6#", random_average(10))

"""
Exercise 7
Write program, that will ask user to write 2 numbers, divise those numbers, and print final result.
Also secure Your code from possible errors.
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


#print("7#", division_check())


"""
Exercise 8
Write a function that will check validation of PESEL number. Function will take string as a value and return 
boolean value. PESEL contains 11 numbers. Last number is a control number. First 10 numbers should be multiple by
following numbers: `1 3 7 9 1 3 7 9 1 3`. Those numbers should be summed, then divided by 10 and finally minus
10. If number You get will be equal to control number PESEL number is correct.
"""


def validate_pesel(data):
    pesel = [int(i) for i in str(data)]
    wage = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    new_list = [pesel[i] * wage[i] for i in range(len(pesel) - 1)]

    result = 10 - (sum(new_list) % 10)

    if result == pesel[-1]:
        return True

    else:
        return False


print("8#", validate_pesel(88042512499))
