# question 1

# question 2

# question 3

# question 4

# question 5

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

