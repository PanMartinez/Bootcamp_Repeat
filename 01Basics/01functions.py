"""
Exercise 1:
Write a function that returns "num" squared 
"""

def squared(num):
    sq = num ** 2
    return (sq)

print ("1#", squared(5))


"""
Exercise 2:
Write a function `multiply(subject, times)`, that returns `subject` multiple by `times`. 
Notice what happen when Yoy use number, and what happen if you use string,
as an argument.

"""


def multiply(subject, times):
    result = subject * times
    return result

print ("2#", multiply(2, 7)) # result of multiplication
print ("2#", multiply(5, "JackDaniels")) # 5 times JackDaniels


"""
Exercise 3
Write a 'power` function that take two arguments:

* `base`: must be
* `exponent`: optional with standard value of 2.

Function must return base value put to `exponent' power.
"""


def power (base, exponent = 2):
    return (base ** exponent)

print ("3#", power(6, 2)) # returns 36
print ("3#", power(6)) # also returns 36


"""
Exercise 4
Write a fuction "convert_to_usd", that takes "zlotys" as a parameter. Function must return given value in dollars.
(take 3.85 PLN as a 1 USD, as a value)
"""


def convert_to_usd(zlotys):
    usd = zlotys / 3.85
    return (usd)

print("4#", convert_to_usd(50))


"""
Exercise 5 
Write a `create_name` function, that takes: `name', `surname`, and `nickname`. Function must return
string with name, nickname and surname connected.
"""


def create_name(name, surname, nickname):
    return name +" "+ nickname + " "+ surname

print("5#", create_name("Marcin", "Plotka", "Martinez"))


"""
Exercise 6
Write a `calculate_net` function that takes 'gross' and 'vat' as a price of buy and tax values.
Function must return netto value of the price
"""


def calculate_net(gross, vat):
    netto = gross / (1 + vat)
    return netto


print("6#", calculate_net(123, 0.23))


"""
Exercise 7
Write a 'square area' function that count and returns square field, taking 2 parameters as
values of it sides
"""

def square_area(x,y):
    area = x*y
    return area

print ("7#", square_area(5,20))


"""
Exercise 8
Write a 'circle_circut' function that takes diameter of a circle, and returns it circumference
"""

def circle_circut(r):
    circ = 2 * 3.1415 * r
    return circ
print ("8#", circle_circut(10))


"""
Exercise 9
Write a function 'dogs_age' that will count dogs age. Function should takes dogs age as parameter.
For 2 first years dogs age is equal to 10.5 of humans age. After this each dogs year is equal to 4 human.
function should return dog's age.
 egz: azor = dogs_age(1.5) == 15.75
 egz: burek = dogs_age(5) == 33
"""

def dogs_age(age):
    if age < 2:
        return age * 10.5
    else:
        return age * 4 + 13

print ("9#", dogs_age(1.5))
print ("9#", dogs_age(5))


"""
Write "chessboard" function that takes 'n' parameter, as an optional.
Standard value of n should be 8. Function must white a chessboard on the console,
made from # and spaces.
"""

def chessboard(n=8):
    for row in range(0, n):
        r = ""
        for col in range(0, n):

            if row % 2 == 1:

                if col % 2 == 0:
                    r += "#"
                else:
                    r += " "
            else:

                if col % 2 == 0:
                    r += " "
                else:
                    r += "#"
        print(r)

print("10#"), chessboard()


"""
Exercise 11
Write "find a number" function that take a number and checking if it is divisible by 4, and return True or False.
"""

def find_a_number(number):
    if number % 4 == 0:
        return True
    else:
        return False

print ("11#", find_a_number(40))
print("11#", find_a_number(34))


"""
Exercise 12
Write a 'histogram' function, that will take a list of numbers, and returns histogram made from "#"
If values, given by user will be different than number, function should return "None".

"""
def histogram(array):
    hist = ""

    for i in array:
         if type(i) == int:
             hist += (i * "#") + "\n"

         else:
             return None

    return hist


h = histogram([2, 6, 3, 1])
m= histogram([1, 2, 'error!'])


print("12#", h)
print("12#", m)


"""
Exercise 13
Write a function that will count a Fibonacci sequence. Function should return n, as a value of this number,
in Fibonacci sequence
"""

def fibonacci(n):

    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print("13#", fibonacci(9))
        