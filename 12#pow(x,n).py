def power(x, n):
    # cases
    if n == 0: return 1 # when power is zero
    if x == 1: return 1 # when base is one
    if x == 0: return 0 # when base is zero

    if x == -1 & n%2 == 0 : return 1
    if x == -1 & n%2 != 0 : return -1

    if n < 0: # if negative power
        x = 1/x
        n = -n

    ans = 1

    while n > 0:
        if n % 2 == 1:  # Check if current bit is 1
            ans *= x
        x *= x  # Square x for next bit
        n //= 2  # Integer division, not float
    return ans

print(power(-2, 4))  