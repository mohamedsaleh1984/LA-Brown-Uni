import math

"""
Task 1: Use Python to fnd the number of minutes in a week.
"""
def minutes_per_week():
    week = 7
    hours = 24
    minutes = 60
    return week*hours*minutes


"""
Task 2: Use Python to find the remainder of 2304811 divided by 47 without using the modulo operator %.
(Hint: Use //.)
"""

def reminder():
    num = 2304811
    div = 47
    quot = num //div
    rem = num - (  quot *  div)
    return rem

"""
Task 3: Enter a Boolean expression to test whether the sum of 673 and 909 is divisible by 3.
"""
def exp():
    result = (673 + 909) % 3 == 0
    print(result)

"""
Task 4: Assign the value -9 to x and 1/2 to y. Predict the value of the following expression, then enter it
to check your prediction:
2**(y+1/2) if x+10<0 else 2**(y-1/2)
"""
def eval():
    ### 2**(y+1/2) if x+10<0 else 2**(y-1/2)
    ### IF (-9+10) => 1 <  0 => false 
    ### 2^0 => 1
    x = -9
    y = 1/2
    print(2**(y+1/2) if x+10<0 else 2**(y-1/2))

"""
Task 5: Write a comprehension over {1, 2, 3, 4, 5} whose value is the set consisting of the squares of the
first five positive integers.
"""
def comprehensive():
    ss = { 1,2, 3, 4, 5}
    v = {x*x for x in ss}
    print(v)
    xx = {x*x for x in {0,2,5,5,-1,-78,52,91} if x > 0}
    print(xx)
    ## print(2**(y+1/2) if x+10<0 else 2**(y-1/2))

"""
Task 6: Write a comprehension over {1, 2, 3, 4}  whose value is the set consisting of the first five powers
of two, starting with 2^0.
"""
def comprehensive2():
    print({2**x for x in  { 1,2, 3, 4}})    

"""
Task 7: The value of the previous comprehension,
{x*y for x in {1,2,3} for y in {2,3,4}}
is a seven-element set. Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value
becomes a nine-element set.
"""
def new_set_with_len9():
    new_set = {x * y for x in {1,2,3} for y in {4,5,7}}
    print(new_set)
    print(len(new_set))

"""
Task 8: Replace {1,2,3} and {2,3,4} in the previous comprehension with two disjoint (i.e. non-overlapping)
three-element sets so that the value becomes a fve-element set.

Used Powers of 2s 2^1, 2^2,....2^6
"""
def comprehensive3():
    T = {x * y for x in {1,2,4} for y in {8,16,32}}
    print(T)


"""
Task 9: Assume that S and T are assigned sets. Without using the intersection operator &, write a comprehension 
over S whose value is the intersection of S and T. 
Hint: Use a membership test in a filter at the end of the comprehension.
Try out your comprehension with S = {1,2,3,4} and T = {3,4,5,6}
"""

def comprehensive4():
    S = {1,2,3,4}
    T = {3,4,5,6}
    new_set = {x for x in S for y in T if x == y}
    print(new_set)

"""
Task 10: Write an expression whose value is the average of the elements of the list [20, 10, 15, 75].
"""
def avg_list():
    list = [20,10,15,75]
    av = sum(list)/len(list)
    print(av)

"""
Task 11: Write a double list comprehension over the lists [A,B,C] and [1,2,3] whose value is the
list of all possible two-element lists [letter, number]. That is, the value is
"""
def comprehension_list():
    new_list = [[x,y] for x in ['A','B','C'] for y in [1,2,3] ]
    print(new_list)
    
"""
Task 12: Suppose LofL has been assigned a list whose elements are themselves lists of numbers. Write an
expression that evaluates to the sum of all the numbers in all the lists. The expression has the form
sum([sum(...
and includes one comprehension. Test your expression after assigning [[.25, .75, .1], [-1, 0], [4,
4, 4, 4]] to LofL. Note that your expression should work for a list of any length.
"""
def LofL():
    l = [[.25, .75, .1], [-1, 0], [4,4, 4, 4]]
    sums = sum([sum(x) for x in l])
    print(sums)

"""
Task 13: Suppose S is a set of integers, e.g. {-4;-2, 1, 2, 5, 0}. Write a triple comprehension whose value
is a list of all three-element tuples (i, j, k) such that i, j, k are elements of S whose sum is zero.
"""
def comprehensive_tuple():
    s = { -4,-2, 1, 2, 5, 0}
    lists = [[i,j,k] for i in s for j in s for k in s if i+j+k == 0]
    tuples = [(i,j,k) for i in s for j in s for k in s if i+j+k == 0]
    print(tuples)
    print(lists)

"""
Task 14: Modify the comprehension of the previous task so that the resulting list does not include (0; 0; 0).
Hint: add a filter.
"""
def comprehensive_tuple2():
    s = { -4,-2, 1, 2, 5, 0}
    tuples = [(i,j,k) for i in s for j in s for k in s if (i+j+k == 0)  ]
    tuples.remove((0, 0, 0))
    print(tuples)


"""
Task 15: Further modify the expression so that its value is not the list of all such tuples but is the first
such tuple.
"""
def comprehensive_tuple3():
    s = { -4,-2, 1, 2, 5, 0}
    tuples = [(i,j,k) for i in s for j in s for k in s if (i+j+k == 0 ) ]
    
    print(tuples)

