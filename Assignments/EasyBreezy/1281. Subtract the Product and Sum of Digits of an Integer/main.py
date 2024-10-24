class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # initialize product and sum
        product = 1
        summ = 0
        # iterate over the digits
        for i in str(n):
            # calc product and sum
            product *= int(i)
            summ += int(i)
        # return difference
        return product - summ
        
        
        


