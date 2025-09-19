def big_factorial(n: int) -> str:
    res = [1]
    for i in range(2, n+1):
        carry = 0
        for j in range(len(res)):
            prod = res[j] * i + carry
            res[j] = prod % 10
            carry = prod // 10
        while carry:
            res.append(carry % 10)
            carry //= 10
    return ''.join(map(str, res[::-1]))