from math import sqrt

def isPrime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(sqrt(n))))

def enumPrimes(start, end):
    return [ n for n in range(start, end) if isPrime(n) ]

print ('Liczby pierwsze: ', enumPrimes(10, 100))