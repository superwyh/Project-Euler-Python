def compute():
    N = 100
    return sum(range(1, N + 1)) ** 2 - sum(i**2 for i in range(1, N + 1))

if __name__ == "__main__":
    print(compute())
