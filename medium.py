def prime(x):
    return x > 1 and all(x % j != 0 for j in range(2, int(x ** 0.5) + 1))


def pdel(n):
    pd = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if prime(d):
                pd.append(d)
            if prime(n // d):
                pd.append(n // d)
    return pd


k = 0
for i in range(10_000, 100_000):
    if len(pdel(i % 1000)) > 2:
        k += 1
print(k)

