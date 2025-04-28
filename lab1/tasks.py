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
    ## No work around this one unless we use ranges.
    _tuples = [(i,j,k) for i in s for j in s for k in s if (i+j+k == 0 ) ]
    tuples = [_tuples[0]]
    print(tuples)


"""
Task 16: Find an example of a list L such that len(L) and len(list(set(L))) are different.
"""
def example():
    List = [1,1,2,3,4,5]
    print(len(List) == len(list(set(List))))

"""
Task 17: Write a comprehension over a range of the form range(n) such that the value of the compre-
hension is the set of odd numbers from 1 to 99.
"""
def use_ranges():
    my_set = {x for x in range(100) if x%2==1}
    print(my_set)

"""
Task 18: Assign to L the list consisting of the first five letters [A,B,C,D,E]. Next, use L in an expression whose value is
[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
Your expression should use a range and a zip, but should not use a comprehension.
"""
def use_zip():
    L = ['A','B','C','D','E']
    nums = list(range(5))
    res = list(zip(nums, L))
    print(res)
    

"""
Task 19: Starting from the lists [10, 25, 40] and [1, 15, 20], write a comprehension whose value is
the three-element list in which the first element is the sum of 10 and 1, the second is the sum of 25 and 15,
and the third is the sum of 40 and 20. Your expression should use zip but not list.
"""
def list_sum():
    L1 = [10, 25, 40]
    L2 = [1, 15, 20]
    res = [x+y for x,y in zip(L1,L2)]
    print(res)

"""
Task 20: Suppose dlist is a list of dictionaries and k is a key that appears in all the dictionaries in dlist.
Write a comprehension that evaluates to the list whose ith element is the value corresponding to key k in
the ith dictionary in dlist.
    Test your comprehension with some data. Here are some example data.
dlist = [{James:Sean, director:Terence}, {James:Roger,director:Lewis}, {James:Pierce, director:Roger}]
k = James

For these data, the value corresponding to k in the first dictionary is 'Sean', the value corresponding to k
in the second dictionary is 'Roger', and the value corresponding to k in the third dictionary is 'Pierce',
so the comprehension should evaluate to ['Sean','Roger','Pierce'].
"""
def using_dic_comprehensions():
    dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger','director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
    k = 'James'
    value = [x[k] for x in dlist if k in x]
    print(value)

"""
Task 21: Modify the comprehension in Task 20 to handle the case in which k might not appear in all the
dictionaries. The comprehension evaluates to the list whose ith element is the value corresponding to key k
in the ith dictionary in dlist if that dictionary contains that key, and 
NOT PRESENT otherwise. One way to solve this is to use a conditional expression. Another way is to use the .get(key, default) method of
dictionaries. Test your comprehension with k = Bilbo and k = Frodo and with the following list of dictionaries:
dlist = [{Bilbo:Ian,Frodo:Elijah},{Bilbo:Martin,Thorin:Richard}] 
For example, with k = Frodo, 
the first dictionary in the list maps 'Frodo' to 'Elijah', and the sec-ond dictionary in the list does not map 'Frodo' to anything, so the comprehension should evaluate to
['Elijah','NOT PRESENT'].
"""
def using_dic_Comprehensions2():
    dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]     
    k = 'Frodo'
    # perfect
    value = [x[k] if k in x else 'NOT PRESENT ' for x in dlist]
    print(value)

"""
Task 22: Using range, write a comprehension whose value is a dictionary. The keys should be the integers
from 0 to 99 and the value corresponding to a key should be the square of the key.
"""
def dic_ranges_comprehensions():
    res = [{x:x**2} for x in list(range(100))]
    print(res)

"""
Task 23: Assign to the variable D the set { red , white , blue }. 
Now write a comprehension that evaluates to a dictionary that represents the identity function on D.
"""
def D_variable():
    D = { 'red' , 'white' , 'blue' }
    iden_dic = {d: d for d in D}
    print(iden_dic)


"""
Task 24: Our system for writing numbers uses decimal notation. For example, the digits (2; 1; 5) represent
the number 2 * 10^2 + 1 * 10^1 + 5 * 10^0. We say for this system that the base is 10, and that the available
digits are 0,1, 2,....., 9.
In binary, the digits (1; 0; 1) represent the number 1*2^2 +0 *2^1 +1 * 2^0.

In this case, the base is 2, and the available digits are 0; 1.
Write a dictionary comprehension using the variables base and digits that evaluates to a dictionary
that maps each three-digit number to the three digits that represent it. For example, if base = 10 then
digits should be the set {0,1,2,..., 9} and the comprehension should evaluate to
{0:(0,0,0), 1:(0,0,1), ..., 999:(9,9,9)}
If base = 2 then digits should be the set f0,1g, and the comprehension should evaluate to
{0:(0,0,0), 1:(0,0,1), 2:(0,1,0),3:(0,1,1), 4:(1,0,0), ...}

"""
def digitSystemMapper():
    res = {num:((num>>2) & 1,(num>>1) & 1,num&1) for num in range(8)}
    print(res)

"""
Task 25: Suppose id2salary is a dictionary that maps some employee IDs (a subset of the integers from
0 to n􀀀1) to salaries. Suppose L is an n-element list whose ith element is the name of employee number i.
Your goal is to write a comprehension whose value is a dictionary mapping employee names to salaries. You
can assume that employee names are distinct.
Test your comprehension with the following data:
id2salary = {0:1000.0, 3:990, 1:1200.50}
names = ['Larry', 'Curly', , 'Moe']
"""
def salaryMapper():
    id2salary = {0:1000.0, 3:990, 1:1200.50}
    names = ['Larry', 'Curly','' , 'Moe']
    keys = id2salary.keys() 
    res = { names[k]:id2salary[k]  for k in keys if names[k] != '' }
    print(res)

"""
Task 26: Define a one-line procedure nextInts(L) specied as follows:
- input: list L of integers
- output: list of integers whose ith element is one more than the ith element of L
- example: input [1; 5; 7], output [2; 6; 8].
"""
def nextInts():
    L = [1, 5, 7]
    output = [x+1 for x in L]
    print(output)

"""
Task 27: Define a one-line procedure cubes(L) specifed as follows:
- input: list L of numbers
- output: list of numbers whose ith element is the cube of the ith element of L
- example: input [1; 2; 3], output [1; 8; 27].
"""
def cubes():
    L = [1, 2, 3]
    output = [x**3 for x in L]
    print(output)

"""
Task 28: Define a one-line procedure dict2list(dct,keylist) with this spec:
- input: dictionary dct, list keylist consisting of the keys of dct
- output: list L such that L[i] = dct[keylist[i]] for i = 0; 1; 2; : : : ; len(keylist) 􀀀 1
- example: input dct={a:A, b:B, c:C} 
and keylist=[b,c,a],
output [B, C, A]
"""
def dict2list():
    dct={'a':'A', 'b':'B', 'c':'C'} 
    keylist=['b','c','a']
    output = [dct[k] for k in keylist]
    print(output)


"""
Task 29: Define a one-line procedure list2dict(L, keylist) specified as follows:
- input: list L, list keylist of immutable items
- output: dictionary that maps keylist[i] to L[i] for i = 0; 1; 2; : : : ; len(L) 􀀀 1
- example: input L=['A','B','C'] and keylist=['a','b','c'],
output {a:A, b:B, c:C}
Hint: Use a comprehension that iterates over a zip or a range.
"""
def list2dict2():
    L=['A','B','C']
    keylist=['a','b','c']
    output = {a:A for (a,A) in zip(keylist,L)}
    print(output)
    
list2dict2()
