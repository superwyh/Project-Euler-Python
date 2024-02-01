import math

def compute():
    n = 600851475143
    for i in range(2, math.isqrt(n) + 1):
        while n % i == 0:
            n //= i
        if n == 1:
            return str(i)
    return str(n)

if __name__ == "__main__":
    print(compute())
