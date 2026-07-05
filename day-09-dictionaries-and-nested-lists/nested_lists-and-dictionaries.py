"""
NESTING A LIST INSIDE A DICTIONARY
Instead of a String value assigned to a key, 
we can replace it with a List. 
You can nest a List in a Dictionary like this:

my_dictionary = {
    key1: [List],
    key2: Value,
}

"""



# See if you can figure out how to print out "Lille" from the nested List called travel_log.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Solution:
print(travel_log["France"][1])


"""
NESTING LISTS INSIDE OTHER LISTS
We've previously seen Nested Lists:
"""

nested_list = ["A", "B", ["C", "D"]]

"""
Do you remember how to get items that are nested deeply in a list? 
Try to print "D" from the list nested_list
"""

#Solution:
print(nested_list[2][1])

"""
NESTING A DICTIONARY INSIDE OF A DICTIONARY
You can also nest a dictionary in a dictionary:

my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
"""

"""
Figure out how to print out "Stuttgart" from the following list:
"""

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

# Solution
print(travel_log["Germany"]["cities_visited"][2])