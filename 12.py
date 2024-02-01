import itertools, math

def compute():
    triangle = 0
    for i in itertools.count(1):
        triangle += i
        if num_divisors(triangle) > 500:
            return str(triangle)

def num_divisors(n):
    divisors = sum(2 for i in range(1, math.isqrt(n) + 1) if n % i == 0)
    return divisors - 1 if math.isqrt(n)**2 == n else divisors

if __name__ == "__main__":
    print(compute())
