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


# Problem 204: Given a complete binary tree, count the number of nodes in faster than O(n) time


# Problem 205: Given an array and a permutation, apply the permutation to the array.
# For example, given the array ["a","b","c"] and the permutation [2,1,0] will return ["c","b","a"]

def prob206(arr, perm):
    arr_return = []
    for item in perm:
        arr_return.append(arr[item])

    return arr_return

# Problem 211: Given a string and a pattern, find the starting indices of all occurences
# of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should
# return [0,7]

def prob211(str, patt):

    if len(patt)>len(str):
        print("invalid pattern and string")
        return
    else:
        list_occ = []
        for i in range(0, len(str)-len(patt)+1):
            if str[i:len(patt)+i] == patt:
                list_occ.append(i);

        return list_occ


# Problem 1439: Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found
# in the matrix by going left-to-right or up-to-down
# For example given the following matrix:
# [['F','A','C','I'],
#  ['O','B','Q','P'],
#  ['A','N','O','B'],
#  ['M','A','S','S']] 
# and the target word 'FOAM', you should return TRUE since it's the leftmost column
# Similarly, given the target word 'MASS', you should return TRUE since its the last row

def prob1439(maxtr,target):
    import numpy as np
    # convert 2 numpy array
    maxtr = np.array(maxtr)
    n,m = maxtr.shape
    
    # left-right checking:
    for i in range(n):
        source = ''
        for j in range(m):
            source = source + maxtr[i][j]
        if source == target:
            return True
            
    # top-down checking:
    for i in range(m):
        source = ''
        for j in range(n):
            source = source + maxtr[j][i]
        if source == target:
            return True    