"""
Sets
"""
s = {1,23,4,5,6,7,6}
print('no duplication ',s)

s2 = {'a',12.32,68,'A','a',1}
print('generic types and sorted',s2)


print('set length ' , len(s2))

print(4 in s)

print(sum(s))

### mutate list
s.add(2)
s.remove(23)
print(sum(s))

### union
print(s | s2)
### intersection
print(s & s2)

## comprehensions
print('before ', s)
v = {2*x for x in s}
print('after ', v)

"""
By adding the phrase if hconditioni at the end of the comprehension (before the closing brace \g"), you
can skip some of the values in the set being iterated over:
"""
o = {x*x for x in {1,2,3,96,7,7} | {5, 7} if x > 2}
##print(o)

### You can write a comprehension that iterates over the Cartesian product of two sets:
t = {x*y for x in {1,2,3} for y in {2,3,4}}
## print(t)



L = [0,10,20,30,40,50,60,70,80,90]
print(L[:5])
print(L[5:])



my_list = list(range(10))
print(my_list)
print(set(my_list))


x = list(zip([1,3,5],[2,4,6]))
print(x)


c = [x*x for x in reversed([4, 5, 10])]
print(c)

dic = {2+1:'thr'+'ee', 2*2:'fo'+'ur'}
print(dic)

hola = { k:v for (k,v) in [(3,2),(4,0),(100,1)] }
print(hola)


keys = [2*x for x in {4:'a',3:'b'}.keys() ]
print(keys)
