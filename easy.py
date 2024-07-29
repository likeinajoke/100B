def deli(n):
    vsedel = [1, n]
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d * d == n:
                vsedel.append(d)
            else:
                vsedel.append(d)
                vsedel.append(n // d)
    return sorted(vsedel)


k = 0
for i in range(100, 500, 5):
    k += len(deli(i))
print(k)

