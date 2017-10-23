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