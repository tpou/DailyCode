# Problem 1: Given a list of number and a number k, return whether any two numbers from the list add up to k
# For ex. given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
#  Bonus: Can you do it in one pass

def prob1(list, k):
    count = 0
    while (count < len(list)):
        for i in range(0,len(list)):
            if (list[i] + list[count] == k):
                return True
                break
        count += 1

    return False

# Problem 2: Given an array of intergers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except the one at i
# What if you  cant use division

def prob2(input_list):
    product = 1
    output_list = []
    for i in range(0, len(input_list)):
        product *= input_list[i]

    for i in range(0, len(input_list)):
        output_list.append(product / input_list[i])
    return output_list

# Problem 3: Given the root to a binary tree, implement serialize(root) to serialize the tree
# into astring and deserialize(root) to deserialize the string back into the root



# Problem 4: Given an array of integers, find the first missing positive integer in linear time and constant space
# In other words, find the lowest positive integer that does not exist in the array. The array
#  can contain duplicates and negative numbers as well

# Problem 5: cons(a,b) construct a pair, car(pair) and cdr(pair) returns the first and the last element of that pair
#  For ex: car(cons(3,4)) return 3, and cdr(cons(3,4) returns 4

def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair


# Problem 198: Given a set of distinct pos integers, find the largest subset such that
#  every pair of elements in the subset(i,j) satisfies either i%i =0 or j%i =0

# Problem 202: Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well
# as 888. 678 is not a palindrome. Do not convert the integer into a string

def prob121(number):
    count = 0
    number_list = []

    while(number>0):
        number_list.insert(0,number % 10)
        count+=1
        number = number//10

    for i in range(0, count//2):
        if (number_list[i] != number_list[count-1-i]):
            palidrome = False
            break
        else:
            palidrome = True

    return palidrome


