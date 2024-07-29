def deli(n):
    vsedel = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d * d == n:
                vsedel.append(d)
            else:
                vsedel.append(d)
                vsedel.append(n // d)
    return sorted(vsedel)


def ch(s):
    mx = max(s)
    s.remove(mx)
    if mx < sum(s):
        mn = min(s)
        s.remove(mn)
        if mn + mx == sum(s):
            return True
        else:
            return False
    else:
        return False


k = 0
for i in range(378450, 500_000):
    if len(deli(i)) >= 4:
        sp = deli(i)[:4]
        if ch(sp):
            print(i, max(deli(i)))
            k += 1
    if k == 7:
        break

