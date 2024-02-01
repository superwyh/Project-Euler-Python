def compute():
    n = 2**1000
    return str(sum(int(c) for c in str(n)))

if __name__ == "__main__":
    print(compute())
