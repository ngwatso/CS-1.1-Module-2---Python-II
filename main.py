"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module that start with the letters "is".
"""
# 1
# YOUR CODE HERE
# import math

# mathFuncs = dir(math)
# filteredList = []

# for x in mathFuncs:
#   if x.startswith("is"):
#     filteredList.append(x)

# print(filteredList)
# print(dir(math))

"""
1. Create a "numbers" list that contains two different integer values and two different floating point values.

2. Create a "strings" list that contains three different strings.

3. Print the 4th number of your numbers list and the 1st string of your strings list.

4. Iterate through your strings list and print each string.
"""
# 2
# YOUR CODE HERE

# numbers = [1, 2, 3.1, 4.2]
# strings = ["Honey", "Sophie", "Pip"]

# print(numbers[3], strings[0])

# for x in strings:
#   print(x)

"""
Below, you'll find a class definition for animals. Create two new animals `cat`
and `dog`. Set `cat` to have a name of "Purrfect", kind of "cat",
and color of "brown". Set `dog` to have a name of "Fido",
kind of "dog", and color of "black".
"""
#  3
class Animal:
    name = ""
    kind = ""
    color = ""
    
    def description(self):
        return "%s is a %s %s." % (self.name, self.color, self.kind)

# Create instances of Animal here and modify the instance attributes
cat = Animal()

cat.name = "Purrfect"
cat.kind = "cat"
cat.color = "brown"

dog = Animal()

dog.name = "Fido"
dog.kind = "dog"
dog.color = "black"

# as described above.

# Should print Purrfect is a brown cat.
print(cat.description())
# Should print Fido is a black dog.
print(dog.description())