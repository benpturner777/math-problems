import numpy as np
import math

# ==========================
# 1) Sum of multiples of a or b below a limit
# ==========================
def sum_multiples(a, b, limit):
    total = 0
    for x in range(limit):
        if x % a == 0 or x % b == 0:
            total += x
    return total

# User-defined parameters
a = 3        # first multiple
b = 5        # second multiple
limit = 1000 # upper bound
print(f'Sum of all multiples of {a} or {b} below {limit} is {sum_multiples(a, b, limit)}')


# ==========================
# 2) Sum of even Fibonacci numbers up to max_fib
# ==========================
max_fib = 4000000
fib_a, fib_b = 1, 2
total_even_fib = 0

while fib_a < max_fib:
    if fib_a % 2 == 0:
        total_even_fib += fib_a
    fib_a, fib_b = fib_b, fib_a + fib_b

print(f'Sum of even Fibonacci numbers up to {max_fib} is {total_even_fib}')


# ==========================
# 3) Largest prime factor of a number
# ==========================
def largest_prime_factor(n):
    factor = 2
    while n > 1:
        if n % factor == 0:
            n /= factor
        else:
            factor += 1
            if factor > n / factor:
                return n
    return n

number_to_factor = 1238745009
print(f'Largest prime factor of {number_to_factor} is {largest_prime_factor(number_to_factor)}')


# ==========================
# 4) Largest palindrome product of two 3-digit numbers
# ==========================
def is_palindrome(n):
    return str(n) == str(n)[::-1]

start = 100
end = 999
max_palindrome = 0

for i in range(end, start - 1, -1):
    for j in range(end, start - 1, -1):
        product = i * j
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product

print(f'Largest palindrome product of two 3-digit numbers is {max_palindrome}')


# ==========================
# 5) Smallest number divisible by all numbers from 1 to n
# ==========================
max_divisor = 20
num = max_divisor
found = False

while not found:
    found = all(num % i == 0 for i in range(1, max_divisor + 1))
    if not found:
        num += 1

print(f'Smallest number divisible by all numbers from 1 to {max_divisor} is {num}')


# ==========================
# 6) Difference between sum of squares and square of sum
# ==========================
max_n = 100
sum_of_squares = sum(i ** 2 for i in range(1, max_n + 1))
square_of_sum = sum(range(1, max_n + 1)) ** 2
difference = abs(sum_of_squares - square_of_sum)

print(f'Difference between sum of squares and square of sum for first {max_n} numbers is {difference}')


# ==========================
# 7) Nth prime number
# ==========================
nth_prime = 10001
primes = [2, 3]
num = 5

while len(primes) < nth_prime:
    for p in primes:
        if num % p == 0:
            break
    else:
        primes.append(num)
    num += 2

print(f'The {nth_prime}th prime number is {primes[-1]}')


# ==========================
# 8) Largest product of k adjacent digits in a number string
# ==========================
number_string = '73167176531330624919225119674426574742355349194934' \
                '96983520312774506326239578318016984801869478851843' \
                '85861560789112949495459501737958331952853208805511' \
                '12540698747158523863050715693290963295227443043557' \
                '66896648950445244523161731856403098711121722383113' \
                '62229893423380308135336276614282806444486645238749' \
                '30358907296290491560440772390713810515859307960866' \
                '70172427121883998797908792274921901699720888093776' \
                '65727333001053367881220235421809751254540594752243' \
                '52584907711670556013604839586446706324415722155397' \
                '53697817977846174064955149290862569321978468622482' \
                '83972241375657056057490261407972968652414535100474' \
                '82166370484403199890008895243450658541227588666881' \
                '16427171479924442928230863465674813919123162824586' \
                '17866458359124566529476545682848912883142607690042' \
                '24219022671055626321111109370544217506941658960408' \
                '07198403850962455444362981230987879927244284909188' \
                '84580156166097919133875499200524063689912560717606' \
                '05886116467109405077541002256983155200055935729725' \
                '71636269561882670428252483600823257530420752963450'
adjacent_digits = 13

max_prod = 0
for i in range(len(number_string) - adjacent_digits + 1):
    prod = 1
    for char in number_string[i:i + adjacent_digits]:
        prod *= int(char)
    if prod > max_prod:
        max_prod = prod

print(f'Largest product of {adjacent_digits} adjacent digits is {max_prod}')


# ==========================
# 9) Pythagorean triple summing to n_sum
# ==========================
n_sum = 1000
found = False

for a in range(1, n_sum):
    for b in range(a, n_sum // 2):
        c = (a ** 2 + b ** 2) ** 0.5
        if c.is_integer() and a + b + c == n_sum:
            print(f'Pythagorean triple that sums to {n_sum}: {a}, {b}, {int(c)}')
            found = True
            break
    if found:
        break


# ==========================
# 10) Sum of primes below max_prime
# ==========================
max_prime = 2000000
primes = [2]

for i in range(3, max_prime, 2):
    is_prime = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

print(f'Sum of primes below {max_prime}: {sum(primes)}')


# ==========================
# 12) First triangle number with over min_divisors
# ==========================
min_divisors = 500
triangle = 0
i = 1

while True:
    triangle += i
    divisors = 0
    for j in range(1, int(math.sqrt(triangle)) + 1):
        if triangle % j == 0:
            divisors += 2  # j and triangle/j
    if divisors > min_divisors:
        print(f'First triangle number with over {min_divisors} divisors: {triangle}')
        break
    i += 1
