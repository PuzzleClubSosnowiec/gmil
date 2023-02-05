import math
from prime_to_100000 import prime_to_100000

# -------------------------------------------------------------------------------------------------
def prime_to(n):
    if(n < 2):
        return []
    if prime_to_100000[-1] < n:
        return None
    size = len(prime_to_100000)
    top = size
    bottom = 0
    while top > bottom:
        mid = int((top + bottom) / 2)
        if prime_to_100000[mid] > n:
            top = mid
        else:
            bottom = mid+1
    return prime_to_100000[:top]

# -------------------------------------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    sqrtn = math.sqrt(n)
    if sqrtn <= 100000:
        for d in prime_to(sqrtn):
            if n % d == 0:
                return False
        return True
    return None
