import math

def compute():
    return str(sum(int(c) for c in str(math.factorial(100))))

if __name__ == "__main__":
    print(compute())
