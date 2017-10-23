from random import randint
import datetime
"""
Exercise 1
Write a function that will take 2 arguments, and return a list, where elements, will be a values,
four times repeat.
"""
def create_list(a,b):
    newlist = []
    newlist.append((a,b)*4)
    return newlist
print ("1#",create_list("Johnnie", "Walker"))
print ("1#", create_list(1,7))


"""
Exercise 2
Write a 'list_keys' function, where 'd' will be a dictionary. Function should return list of keys from  this dictionary
"""

def list_keys(d):
    result = []
    for key in d.keys():
        result.append(key)
    return result

data = {
    "single malt" : "Macallan",
    "bourbon" : "Four Roses",
    "blend" : "Chivas Regal",
    "irish" : "Jameson" }

print("2#", list_keys(data))

"""
 Exercise 3
 Write 'max_length' function that will take list of words. Function should return list of words
 shorter than 6 letters.
"""
def max_length(list):
    newlist = []
    for letter in list:
        if len(letter) < 6:
            newlist.append(letter)
    return newlist

print ("3#", max_length(["water", "yeast", "distillery", "barley", "heart"]))


"""
Exercise 4
Write a 'summ' function where 'numbers' will be a list of numbers any type. Function should return sum of
all elements of a list.
"""

def summ(numbers):
    return sum(numbers)

print ("4#", summ([1,2,6,8,18,0.34]))

"""
Exercise 5
Write a'mean' function where 'numbers', will be a list of numbers any type.
Function should return arithmetic mean of all elements from a list.
"""

def mean(numbers):
    return sum(numbers) / len(numbers)

print ("5#", mean([1,4,6,7,2,42]))


"""
Ecercise 6
Write a 'message' function that will take dictionary as parameter: Keys of dict should be: 
'name', 'role' and 'movie'. Function should return string in a format "In 'movie', 'name' is a 'role'.".
If there will be a key that is not in dict, function should return None
"""
def message(dict):
    result = "In {}, {}, is a {}."
    if "name" not in dict or "role" not in dict or "movie" not in dict:
        return None
    else:
        return result.format(dict["movie"],dict["name"],dict["role"])

dictionary = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print("6#", message(dictionary))


"""
Exercise 7
Write a d6 function that will simulate dice throw. 'num' will be parameter, what will simulate number of throws.
Function should return sum, those numbers

"""

def d6(num):
    result = 0
    for i in range (0, num):
        result += randint(1, 6)
    return result

print ("7#", d6(5))


"""
Exercise 8
Write "tomorrow" function that will return tommorow date:
"""

def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)
print ("8#", tomorrow())



"""
Exercise 9
Write a "make_tuple" function that will take 4 parameters (a,b,c,d) last twooptional with standard values of 3 and 4
Return a tuple of values of parameters.
"""

def make_tuple(a,b,c=3,d=4):
    return (a, b, c, d)
print ("9#", make_tuple("Yamazaki", "Sherry Cask Edition" ))



"""
Exercise 10
Write "find first and last" function that will take tuple or list.
Return a tuple what will contain first and last element of argument
"""
def find_first_and_last(array):

    return (array[0], array[-1])

print ("10#", find_first_and_last([3,4,5,5,5,6,4,4,3,1]))


"""
Exercise 11
Write a 'format date' function that will take 3 parameters: 'day', 'month' and 'year'
Function should check if date is valid: Month should be in 1 12 range. Day should be 30, 31 or 28 in july
(assume that is 28 all the time) if something will be wrong function should return None:
Function should return string in "day, month, year" format
"""
def format_date(day, month, year):

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_names = ["january", "february", "march", "april", "may", "june",
                   "july", "august", "september", "october", "november", "december"]

    if month in range (1, 13):
        if months[month -1] >= day > 0:
            return "{} {} {}".format(day, month_names[month -1], year)
        else:
            return None

print ("11#", format_date(20, 10, 2017))
print ("11#", format_date(30, 2, 2015))


"""
Exercise 12
Write a "find_boundaries_ function that will take list of numbers. function should return the biggest and the smallest
numbers from a list. If there will be any non int value on list it should be ignored.
"""

def find_boundaries(array):
    new_list = [i for i in array if type(i) == int or type (i) == float]
    return min(new_list) , max(new_list)

print ("12#", find_boundaries([1, 5, 2, 3.5, -1]))
print( "12#", find_boundaries([0, 2, "a kuku!", 10]))

"""
Exercise 13
Write a Censor function that will take string as an argument. Function should search for bad words:
('Java', 'C#', 'Ruby', 'PHP'). If it find bad word should transform it into "****" and return new string.
"""
def censor(array):
    bad_words = ["Java", "PHP", "Ruby", "C#"]
    words = array.split()
    i = 0
    for word in words:
        if word in bad_words:
            words[i] = "****"

        i +=1
    return " ".join(words)


print ("13#", censor("Java is the best, but PHP is the bestest!"))

"""
Exercise 14
Write a 'check palindrome' function that will take one word, and check if it's pallindrome.
Function sould return True or False
"""

def check_palindrome(word):
    if str(word) == str(word)[::-1]:
        return True
    else:
        return False

print ("14#", check_palindrome("kajak"))
print ("14#", check_palindrome("glenfarclas"))