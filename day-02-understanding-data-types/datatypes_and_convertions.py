# We can access to each character of the string by selecting it position like an array 
# (at the end of the day, a string is a chars array)

print("Hello"[0]) # prints H
print("Hello"[-1]) # prints the last character in the string: o
print("Hello"[-3]) # prints the third character starting from the end


# type() function
print(type("Hello")) # it prints the type of our data

# Type Conversion
print(int("123") + int("456"))
int()
float()
str()
bool()
print("Hello" + 3) # ERROR, we just can concatennate strings, not strings and ints or other datatype