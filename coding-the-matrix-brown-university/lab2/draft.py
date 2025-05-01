from vec import Vec
import copy


  
def neg(v):
    """
    Returns the negation of a vector.

    Consider using brackets notation v[...] in your procedure
    to access entries of the input vector.  This avoids some sparsity bugs.

    >>> u = Vec({1,3,5,7},{1:1,3:2,5:3,7:4})
    >>> -u
    Vec({1, 3, 5, 7},{1: -1, 3: -2, 5: -3, 7: -4})
    >>> u == Vec({1,3,5,7},{1:1,3:2,5:3,7:4})
    True
    >>> -Vec({'a','b','c'}, {'a':1}) == Vec({'a','b','c'}, {'a':-1})
    True
    """
    # return a new copy of the vector
    #print("========================================")
    negated_f = {k: -v[k] for k in v.f}
    return Vec(v.D, negated_f)

u = Vec({1,3,5,7},{1:-1,3:2,5:3,7:4})
print('before ', u)

new = neg(u)
print('neg ', new)

negneg = neg(neg(u))
print('negneg ', negneg)


## Test Vectors
# a = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2})
# b = Vec({'a','e','i','o','u'}, {'o':4,'u':7})
# c = Vec({'a','e','i','o','u'}, {'a':0,'e':1,'i':2,'o':4,'u':7})

# def add2(u,v):

#     u.D = set(u.D)
#     for key in v.D:
#         u.D.add(key)

#     for key in v.f:
#         if key in u.f:
#             u.f[key] = u.f[key] + v.f[key]
#             # print("key is ", key, " value is ", u.f[key])
#         else:
#             # print(f"Adding new value { v.f[key]} for key :{key }")
#             u.f[key] =  v.f[key]
#     return u

# def add(u,v):
#     # Domain
#     D = set(u.D)#|set(v.D)
#     print("D ", D)  
#     # Fields
#     f = {}
#     # push all values from vector
#     for key in u.D:
#         if key in u.f:
#             f[key]= u.f[key]
#         else:
#             f[key] = 0
    
#     # add v to current
#     for key in v.D:
#         # key found in both
#         if key in v.f and key in f:
#             f[key] = f[key] + v.f[key]
#         if key in v.f and key not in f:
#             f[key] = v.f[key]
#         elif key not in v.D:
#             f[key] = 0    
    
#     # f = sorted(f)
#     new_vec = Vec(D,f)
#     return new_vec




d = Vec({'x','y','z'}, {'x':2,'y':1})
e = Vec({'x','y','z'}, {'z':4,'y':-1})
f = Vec({'x','y','z'}, {'x':2,'y':0,'z':4})

def add3(u,v):
    domain = set(u.D | v.D)
    result = {}

    for k in u.f.keys():
        result[k] = u.f[k]
    
    # print('u.f ', result)

    for key in v.f.keys():
         # print(f'current key {key}')
        print('changes ', result)

        if key in u.f:
            result[key] = v.f[key] + u.f[key]
            # addition
            print(f'addition {v.f[key]}+{u.f[key]}={result[key]}' )
        else:
            result[key] = v.f[key]
            print(f'inserted {key} => {result[key]}' )
            
    return Vec(domain,result)

# n = add3(d,e)
# print(n)
# print(f)

# print(n.D)
# print(f.D)

# print(n.f)
# print(f.f)

# res = n == f
# print('are equal ',res)

# print("Testing Vector D" ,f.D)
# print("Result Vector D",new_vec.D)

# print("Testing Vector f",f.f)
# print("Result Vector f",new_vec.f)



    # # Domain
    # D = set(u.D)|set(v.D)
    # # Fields
    # f = {}
    # # push all values from vector
    # for key in u.D:
    #     if key in u.f:
    #         f[key]= u.f[key]
    #     else:
    #         f[key] = 0
    
    # # add v to current
    # for key in v.D:
    #     # key found in both
    #     if key in v.f and key in f:
    #         f[key] = f[key] + v.f[key]
    #     if key in v.f and key not in f:
    #         f[key] = v.f[key]
    #     elif key not in v.D:
    #         f[key] = 0    
    
    # new_vec = Vec(D,f)
    # return new_vec





    # def add(u,v):
    #     u.D = set(u.D)
    #     for key in v.D:
    #         u.D.add(key)

    #     for key in v.f:
    #         if key in u.f:
    #             u.f[key] = u.f[key] + v.f[key]
    #             # print("key is ", key, " value is ", u.f[key])
    #         else:
    #             # print(f"Adding new value { v.f[key]} for key :{key }")
    #             u.f[key] =  v.f[key]
    #     return u