from vec import Vec,GF2_Vec

"""
Problem 1: For vectors v = [-1; 3] and u = [0; 4], find the vectors v + u, v - u, and 3v - 2u.
"""
def problem1():
    v = Vec({'a','b'}, {'a':-1,'b':3})
    u = Vec({'a','b'}, {'a':0,'b':4})

    v_plus_u = v+u
    print(v_plus_u)
    mul_v_u = 3*v-2*u
    print(mul_v_u)

"""
Problem 2: Given the vectors v = [2;􀀀1; 5] and u = [􀀀1; 1; 1], find the vectors v + u, v - u, 2v - u,
and v + 2u.
"""
def problem2():
    v = Vec({'a','b','c'}, {'a':2,'b':-1,'c':5})
    u = Vec({'a','b','c'}, {'a':-1,'b':1,'c':1})

    res = v + u
    print(res)
    res = v - u
    print(res)
    res = 2*v - u
    print(res)
    res = v +2*u
    print(res)
    
"""
Problem 3: For the vectors v = [0; one; one] 
            and u = [one; one; one] over GF(2), find v+u and v+u+u.
"""
def problem3():
    v = GF2_Vec([0,1,1])
    u = GF2_Vec([1,1,1])
    res = v+u
    print(res)

"""
    Sum of vectors a..f is equal to u
"""

def problem4():
    a = GF2_Vec([1,1,0,0,0,0,0])
    b = GF2_Vec([0,0,0,1,1,0,0])
    c = GF2_Vec([0,1,1,0,0,0,0])
    d = GF2_Vec([0,0,0,0,1,1,0])
    e = GF2_Vec([0,0,1,1,0,0,0])
    f = GF2_Vec([0,0,0,0,0,1,1])

    u_s = [a,b,c,d,e,f]
    u1 = GF2_Vec([0,0,1,0,0,1,0])
    u2 = GF2_Vec([0,1,0,0,0,1,0])
    
    u1.revel()
    

problem4()


