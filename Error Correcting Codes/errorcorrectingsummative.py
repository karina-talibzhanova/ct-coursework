import numpy as np


# function HammingG
# input: a number r
# output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2 ** r - 1

    # construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2 ** (r - i - 1))
    for j in range(1, r):
        for k in range(2 ** j + 1, 2 ** (j + 1)):
            pi.append(k)

    # construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i + 1))

    # construct H'
    H = []
    for i in range(r, n):
        H.append(decimalToVector(pi[i], r))

    # construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n - r):
        GG.append(decimalToVector(2 ** (n - r - i - 1), n - r))

    # apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    # transpose
    G = [list(i) for i in zip(*G)]

    return G


# function decimalToVector
# input: numbers n and r (0 <= n<2**r)
# output: a string v of r bits representing n
def decimalToVector(n, r):
    v = []
    for s in range(r):
        v.insert(0, n % 2)
        n //= 2
    return v


# question 1
def message(a):
    r = 2
    while True:
        if 2**r - 2*r - 1 >= len(a):
            break
        else:
            r += 1

    m = []

    k = 2**r - r - 1
    l = decimalToVector(len(a), r)
    a = decimalToVector(int(''.join(str(i) for i in a), 2), len(a))
    z = decimalToVector(0, k - (len(a) + r))

    m.extend(l+a+z)

    return m


# question 2
def hammingEncoder(m):
    r = 2
    while True:
        if 2**r - r - 1 == len(m):
            break
        elif 2**r - r - 1 > len(m):
            return []
        r += 1

    generator = hammingGeneratorMatrix(r)

    encoded = np.matmul(m, generator)

    encoded_ls = []

    for i in encoded:
        encoded_ls.append(i % 2)

    return encoded_ls


# question 3
def hammingDecoder(v):
    r = 2
    while True:
        if 2**r - 1 == len(v):
            break
        elif 2**r - 1 > len(v):
            return []
        r += 1

    hamming = np.zeros((r, 2**r - 1), dtype=np.int)

    for i in range(hamming.shape[1]):
        hamming[:, i] = decimalToVector(i + 1, r)

    syndrome = np.matmul(v, hamming.transpose())

    syndrome_ls = []

    for i in syndrome:
        syndrome_ls.append(str(i % 2))

    index = int(''.join(syndrome_ls), 2) - 1

    if index < 0:
        return v
    else:
        if v[index] == 0:
            v[index] = 1
        else:
            v[index] = 0

    return v


# question 4
def messageFromCodeword(c):
    r = 2
    while True:
        if 2**r - 1 == len(c):
            break
        elif 2**r - 1 > len(c):
            return []
        r += 1

    indices = [2 ** i - 1 for i in range(r)]

    c = [val for index, val in enumerate(c) if index not in indices]

    return c


# question 5
def dataFromMessage(m):
    r = 2
    while True:
        if 2**r - r - 1 == len(m):
            break
        elif 2**r - r - 1 > len(m):
            return []
        r += 1

    l = int(''.join(str(i) for i in m[:r]), 2)
    if l > len(m) - r:
        return []
    a = m[r:r + l]
    z = m[r + l:]
    for j in z:
        if j != 0:
            return []

    return a


# question 6
def repetitionEncoder(m, n):
    return m*n


# question 7
def repetitionDecoder(v):

    if v.count(1) > len(v)//2:
        return [1]
    elif v.count(0) > len(v)//2:
        return [0]
    else:
        return []

