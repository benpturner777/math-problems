#All code aims to take less than 1 minute to compute.

import numpy as np 
import math 

# 1) Find the sum of all the multiples of 3 or 5 below 1000
def sum_multiples(a,b,limit):
    totalsum = 0 
    for x in range(limit):
        if x % a == 0 or x % b == 0:
            totalsum += x 
    return totalsum
a,b,limit = 3,5,1000

print(f'sum of all the multiples of {a} or {b} bellow {limit} is {sum_multiples(a,b,limit)}')


# 2) Sum of Fibonacci even numbers up to 4 million 
a, b = 1, 2     
totalsum = 0   
while a < 4000000:
    if a % 2 == 0:
        totalsum += a 
        a, b = b, a + b
    else:
        a, b = b, a + b
        totalsum += 0
print(f'sum of Fibonacci even numbers up to 4 million is {totalsum}')


# 3) Largest prime factor of 600851475143
def largestprimefactor(n):
    factor = 2 
    while n > 1: 
        if n % factor == 0:
            n /= factor 
        else:
            factor += 1    
            if factor > n / factor:
                return n 
    return n 
print(f'largest prime factor of "n" is {largestprimefactor(1238745009)}') 


# 4) Largest palindromic number that's a product of two 3-digit numbers
def palindromic(n):
    return str(n) == str(n)[::-1]

max_palindrome = 0 
product = 0 
prod_1 = 0
prod_2 = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        product = i * j 
        if palindromic(product) == True and product >= max_palindrome:
            max_palindrome = product
            prod_1 = i 
            prod_2 = j
print(f'largest palindrome product of two 3 digit numbers is {max_palindrome}')


# 5) Smallest positive number that is evenly divisible by all of the numbers from 1 to 20
smallestlcm = 0 
divide = 7  # All numbers below 7 are factors of numbers between 7 & 20.
num = 2520 
while divide <= 20:
    if num % divide == 0: 
        divide = divide + 1 
    else:
        divide = 7 
        num = num + 1 
print(f'lcm of all positive integers up to 20 is {num}')


# 6) Difference between the sum of the squares and square of the sum (first 100 numbers)
import numpy as np 
difference = 0 
totalsum1 = 0 
totalsum2 = 0

for x in range(101): 
    x = x ** 2 
    totalsum1 += x 

for y in range(101):
    totalsum2 += y 
totalsum2 = totalsum2 ** 2

difference = np.abs(totalsum1 - totalsum2)
print(f'the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {difference}')


# 7) 10001st prime number 
num = 5
primes = [2, 3]
while len(primes) <= 10000: 
    for i in primes:
        if num % i == 0:
            break 
    else:
        primes.append(num)
    num += 2
print(f'10001st prime number is {primes[-1]}')


# 8) 13 adjacent digits that create the largest product
adjlist = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

product = 1 
maxprod = 1

for i in range(0, len(adjlist) - 12):
    blocks13 = adjlist[i:i + 13]
    product = 1
    for char in blocks13:
        product *= int(char)
        if product > maxprod:
            maxprod = product       
print(f'largest 13 digit product is {maxprod}')


# 9) A Pythagorean triple that sums to 1000 - the triplet's product
for i in range(999):
    for j in range(500):
        h = (i ** 2 + j ** 2) ** 0.5
        if int(h) == h:
            if i + j + h == 1000:
                print(f'pythagorean triple that sums to 1000: {i}, {j}, {h}')


# 10) Sum of all primes below 2 million 
primes = [2]
print(primes)
is_prime = True

for i in range(3, 2000000, 2): 
    for p in primes: 
        is_prime = True
        if p * p > i:
            break      
        if i % p == 0:
            is_prime = False 
            break 
    if is_prime == True: 
        primes.append(i)

sumprimes = sum(primes)
print(f'sum of primes below 2 million: {sumprimes}')


# 12) First triangle number with over 500 divisors 
trinum = 0 
tri500 = 0
divisors = []

for i in range(1, 99999, 1): 
    trinum += i   
    for j in range(1, math.floor(np.sqrt(trinum)) + 1):
        if trinum % j == 0:
            divisors.append(j)
            divisors.append(trinum)
    if len(divisors) >= 500:
        tri500 = trinum
        print(f'first triangle number with 500 divisors: {tri500}')
        break
    else:
        divisors = []


