def isPP(n):
    m = int(n ** 1/2)
    for i in range(2, m+1):
        k = 0
        while i ** k < n:
            k += 1
        if i ** k == n:
            return [i, k]
    return None


print(isPP(243))
