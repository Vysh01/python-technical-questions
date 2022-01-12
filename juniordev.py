# Write a function to add two numbers
def add_nums(a, b):
    sum = a + b
    return sum


# Driver code
sum = add_nums(10, 23)
print(sum)


# Write a function to add two number provided by user input
def add_from_input():
    number1 = input("First number: ")
    number2 = input("Second number: ")

    # Adding two numbers
    # User might also enter float numbers
    sum = float(number1) + float(number2)
    return sum


# Driver code
sum = add_from_input()
print("Sum is:", sum)


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


# Write a program to reverse a list in Python
def reverse_list(lst):
    lst.reverse()
    return lst


# Driver code
lst = [10, 11, 12, 13, 14, 15]
print(reverse_list(lst))
