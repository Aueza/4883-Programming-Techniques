# My methodology for this problem was explained by chatGPT as it recommened a process 
# called Exoponentiation by Squaring. A good example to get a basic understanding of
# the process is this. If we want to find 2^4, instead of multiplying x by 2 four times,
# we compute 2^2, then square that (2^2)^2, so we cut our computations in half. 
# This leads us to an O(log n) solution rather than a O(n) solution,
# which allows us to compute the larger exponent values more efficiently.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # exponentiation function declaration
        def exponentiation(base, exp):
            t = 1
            while(exp > 0): 
                # for cases where exponent is not an even value
                if (exp % 2 != 0):
                    t = (t * base)
        
                base = (base * base)
                # halve the exponent valuee
                exp = int(exp / 2)
            return t
        # handling edge cases
        if n == 0:
            return 1
        elif x == 0:
            return 0
        elif n < 0:
            return 1/exponentiation(x, -n)
        else:
            return exponentiation(x, n)
