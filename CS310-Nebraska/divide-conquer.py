import math
import copy

def linearSearchIterative(a,key):
    """
    Returns and index at which the key exists, None if no such element
    """
    for i in range(0,len(a)):
        if a[i] == key:
            return i
    return None

def linearSearchDivideConquer(a, left,right,key):
    """
    Returns and index at which the key exists, None if no such element
    using Divide and Conquer approach
    """
    if left > right:
        return None
    if left == right:
        if a[left] == key:
            return left
        else:
            return None
        
    mid = math.floor((left + right) /2)
    # search the left side
    res = linearSearchDivideConquer(a,left,mid,key)
    if res is not None:
        return res
    return linearSearchDivideConquer(a,mid+1,right, key)

"""
Search Demo
    a = [5,2,9,3,2,1,0,9,4,7]
    key = 2
    index = linearSearchIterative(a,key)
    print("Linear ", index)
    index = linearSearchDivideConquer(a,0,len(a)-1,key)
    print("Divide-Conquer ", index)
"""

a = 2
n = 1110
m = 17
# result = a**n % m



def fast_exponentiation(a, n, m):
    result = 1
    a = a % m  # Ensure a is within the modulus
    
    while n > 0:
        if n % 2 == 1:  # If n is odd, multiply result with a
            result = (result * a) % m
        a = (a * a) % m  # Square a
        n = n // 2  # Divide n by 2
    
    return result

def fast_exponentiation_bitwise(a, n, m):
    result = 1
    a = a % m  # Ensure a is within modulus
    
    while n > 0:
        if n & 1:  # If the least significant bit is 1
            result = (result * a) % m
        a = (a * a) % m  # Square a
        n = n >> 1  # Right shift n (equivalent to n // 2)
    
    return result

def fast_exponentiation_bit_power(a, n, m):
    result = 1
    a = a % m  # Ensure a is within modulus
    
    while n > 0:
        if n % 2 == 1:  # Check if the current bit is 1 (instead of n & 1)
            result = (result * a) % m
        a = (a * a) % m  # Square a
        n = n // 2  # Equivalent to right shift (n >> 1)
    
    return result

def compute_a_pow_n_mod_m(a,n,m):
    binary1 = bin(n) 
    binary = binary1[2:] # 0b11010 = 26
    binary = binary[::-1]
    result = 1
    a = a % m
    for i in range(len(binary)):
        if binary[i] == '1':
            result = (result * a ) % m
        a = (a * a) % m
    
    return result


res = fast_exponentiation(a,n,m)
print(f"{a}^{n} mod {m} fast_exponentiation = {res}")
res = fast_exponentiation_bitwise(a,n,m)
print(f"{a}^{n} mod {m} fast_exponentiation_bitwise = {res}")
res = fast_exponentiation_bit_power(a,n,m)
print(f"{a}^{n} mod {m} fast_exponentiation_bit_power = {res}")
res = compute_a_pow_n_mod_m(a,n,m)
print(f"{a}^{n} mod {m} compute_a_pow_n_mod_m = {res}")


def simpleEuclid(a,b):
    while b != 0:
        t = b
        b = a % t
        a = t
    return a



print(f'simpleEuclid (1768,184) => {simpleEuclid(1768,184)}')






















    # product = 1
    # print("len ", len(binary))

    # for i in range(len(binary)):
    #     print(i, ' -> ', binary[i])
    # print("--------------------------")
   

    # for i in range(len(binary)-1,-1,-1):
    #     print(i,'-')
    #     print(binary[i])
    #     # if i == 0:
    #     #     product = 1 if binary[i]=='1' else 1
        
    #     # term = pow(term,2) % m
    #     # if binary[i] == '1':
    #     #     product = (product * term) % m
    
