###### BASICS ######

# Write a program to find maximum of two numbers
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


# Driver code
a = 2
b = 4
print(maximum(a, b))


# Write a program to add two number provided by user input
def add_from_input():
    number1 = input("First number: ")
    number2 = input("Second number: ")

    # Adding two numbers
    # User might also enter float numbers
    mysum = float(number1) + float(number2)
    return sum


# Driver code
mysum = add_from_input()
print("Sum is:", sum)


# Write a program to print inverted star pattern
def print_star(n):
    for i in range(n, 0, -1):
        print((n - i) * ' ' + i * '*')


# Driver code
print_star(10)


###### LISTS ######
# Write a program to find the largest number in a list
def largest(arr):
    # Initialize maximum element
    max = arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


# Driver code
arr = [10, 324, 45, 90, 9808]
larg = largest(arr)
print("Largest in given array is:", larg)


# Write a program to interchange first and last elements in a list
def swap_list(mylist):
    size = len(mylist)
    # Swapping
    temp = mylist[0]
    mylist[0] = mylist[size - 1]
    mylist[size - 1] = temp

    return mylist


# Driver code
mylist = [12, 35, 9, 56, 24]
print(swap_list(mylist))


###### STRING OPERATIONS ######

# Write a program to reverse words of string
def rev_sentence(sentence):
    # first split the string into words
    words = sentence.split(' ')

    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return reverse_sentence


# Driver Code
input = 'TheCodeCIty'
print(rev_sentence(input))


# Write a program to split and join string based on delimiter
def split_string(string):
    # Split the string based on space delimiter
    list_string = string.split(' ')

    return list_string


def join_string(list_string):
    # Join the string based on '-' delimiter
    string = '-'.join(list_string)

    return string


# Driver Function
string = 'The Code City'

# Splitting a string
list_string = split_string(string)
print(list_string)

# Join list of strings into one
new_string = join_string(list_string)
print(new_string)


###### DICTIONARY OPERATIONS #######
# Write a program to find the sum of items in a dictionary
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final


# Driver Function
mydict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(mydict))

# Write a program to convert key-value to flat dictionary
test_dict = {'month': [1, 2, 3],
             'name': ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert key-values list to flat dictionary
# Using dict() + zip()
res = dict(zip(test_dict['month'], test_dict['name']))

# printing result
print("Flattened dictionary : " + str(res))

###### TUPLE OPERATIONS ######

# Unpacking a given Tuple
a = ("MIT", 5000, "IT")

# this lines UNPACKS values
# of variable a
(college, student, type_ofcollege) = a

# print college name
print(college)

# print no of student
print(student)

# print type of college
print(type_ofcollege)


###### DATETIME OPERATIONS ######

# Write a program to convert 12 hour format to 24 hour format
def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


# Driver Code
print(convert24("08:05:45 PM"))

# Write a program to convert date string to timestamp in python
import datetime


def get_timestamp(timest):
    element = datetime.datetime.strptime(timest, "%d/%m/%Y")
    timestamp = datetime.datetime.timestamp(element)
    return timestamp


# Driver Code
timestring = "20/01/2020"
print(get_timestamp(timestring))

###### REGEX ######
# Write a program to check if String Contain Only Defined Characters using Regex
import re


def check(str, pattern):
    # _matching the strings
    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")


# _driver code
pattern = re.compile('^[1234]+$')
check('2134', pattern)
check('349', pattern)


###### FILE HANDLING ######
# Write a program to read give file word by word
def read_word(filename):
    with open(filename, 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                print(word)


# DRIVER CODE
read_word('file.txt')
