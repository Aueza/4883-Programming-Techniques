class Solution:
    def hammingWeight(self, n: int) -> int:
        # convert num to binary and format.
        binary = bin(n)
        binary = binary[2:]
        count = 0
        # for every set bit increment count.
        for digit in binary:
            if digit == "1":
                count += 1
        return count
