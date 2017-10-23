"""
Exercise 1:
Write a function that returns "num" squared 
"""

def squared(num):
    sq = num ** 2
    return (sq)

print (squared(5))


"""
Exercise 2:
Write a function `multiply(subject, times)`, that returns `subject` multiple by `times`. 
Notice what happen when Yoy use number, and what happen if you use string,
as an argument.

"""


def multiply(subject, times):
    result = subject * times
    return result

print (multiply(2, 7)) # result of multiplication
print (multiply(5, "JackDaniels")) # 5 times JackDaniels


"""
Exercise 3
Write a 'power` function that take two arguments:

* `base`: must be
* `exponent`: optional with standard value of 2.

Function must return base value put to `exponent' power.
"""


def power (base, exponent = 2):
    return (base ** exponent)

print (power(6, 2)) # returns 36
print (power(6)) # also returns 36


"""
Exercise 4
Write a fuction "convert_to_usd", that takes "zlotys" as a parameter. Function must return given value in dollars.
(take 3.85 PLN as a 1 USD, as a value)
"""


def convert_to_usd(zlotys):
    usd = zlotys / 3.85
    return (usd)

print(convert_to_usd(50))


"""
Exercise 5 
Write a `create_name` function, that takes: `name', `surname`, and `nickname`. Function must return
string with name, nickname and surname connected.
"""


def create_name(name, surname, nickname):
    return name +" "+ nickname + " "+ surname

print(create_name("Marcin", "Plotka", "Martinez"))


"""
Exercise 6
Write a `calculate_net` function that takes 'gross' and 'vat' as a price of buy and tax values.
Function must return netto value of the price
"""


def calculate_net(gross, vat):
    netto = gross / (1 + vat)
    return netto


print(calculate_net(123, 0.23))