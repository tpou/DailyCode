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

# Probelm 1414[Easy]: Determine whether there exists one-to-one character mapping from one string s1 to another s2
# For example, given s1='abc' and s2='def' return True since we can map a to d, b to e, and c to f
# Given s1='foo' and s2='bar' return False because 'o' cannot map to two characters

def prob1414(s1,s2):
    if len(s1) != len(s2):
        print('Two strings must have the same length!')
        return
    else:
        mydict = {}
        for idx, char in enumerate(s1):
            mydict[s1[idx]] = s2[idx]
            
        mykeys = list(mydict.keys())
        mykeys.sort()

        mydict_sort = {i:mydict[i] for i in mykeys}

        a= mydict_sort.popitem()
        return a

# Problem 1439[Easy]: Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found
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
    return False
    
# Problem 1456[Easy]: Given a string, returing the first recurring character in it or null if 
# there is no recurring character
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null

# Problem 1436[Easy]: Given an array of elements, return the length of the longest subarray where
# all its elements are distinct
# For example, given the array [5,1,3,5,2,3,4,1] return 5 as the longest subarray of distinct element
# [5,2,3,4,1]


# Problem 1453[Easy]: The same as problem 206

def prob1456(str):
    for idx, char in enumerate(str):
        i = idx
        while i < (len(str)-1):
            if char == str[i+1]:
                return char
            else:
                i+=1
    return None

# Problem 1460[Easy]: a fixed point in an array is an element whose value is equal to its index.
# Given a sorted array of distinct elements, return a fixed point if exists. Otherwise, return False
# For example, given [-6,0,2,40] return 2. Given [1,5,7,8] return False

def prob1460(arr):
    for idx, ele in enumerate(arr):
        if idx == ele:
            return ele
    return False    

# Problem 1463[Easy]: Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythagorean triplet
# (a,b,c) is defined by the equation a^2 + b^2 = c^2 

def prob1463(arrint):
# First, square each element in the array
    arrint_sq = [x*x for x in arrint]
    arrint_sq.sort() # sort the square array in the ascending order
    n = len(arrint_sq)
    # move c from the largest value, a from left, b from right just 1 order from c
    # checking the pythago conditions, if not move a and b accordingly until they coincidently meet. Loop the next c
    for i in range(n-1,1,-1):
        c = arrint_sq[i]
        left, right = 0, i-1
        a = arrint_sq[0]
        b = arrint_sq[i-1]

        while left < right:
            a = arrint_sq[left]
            b = arrint_sq[right]
            if a + b == c:
                return True
            elif a + b > c:
                right -=1
            else:
                left +=1    

    return False


