import math

def is_prime(num):
    if num < 2:
        return False
    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True

def sum(array):
    suma = 0
    for x in array:
        if( is_prime( array[x] ) ):
            suma= suma + array[x]
    return suma 
