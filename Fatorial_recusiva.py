def fatorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n - 1) * n
