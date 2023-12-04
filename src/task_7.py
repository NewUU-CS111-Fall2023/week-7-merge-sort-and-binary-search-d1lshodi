def recursivePow(x, n):
    if n == 0:
        return 1
    else:
        return x * recursivePow(x, n - 1)