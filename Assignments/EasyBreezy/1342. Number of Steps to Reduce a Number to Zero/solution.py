class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        # special case
        if num == 0:
            return steps

        # reduce number to zero.
        while num > 0:
            steps += 1
            # if num is even, div by 2.
            if num % 2 == 0:
                num /= 2
            # else subtract by 1 to get even number.
            else:
                num -= 1
        # return total steps.
        return steps
                
