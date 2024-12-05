class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sort nums and init answer list
        sortedNums = nums + []
        sortedNums.sort()
        ans = []

        # for each num in nums
        for indx in range(len(nums)):
            # slice the sorted list to add everything before the first occrence of our number.
            # append the length of this list, which is the number of numbers that
            # are less than our target, to our ans list.
            temp = sortedNums[:sortedNums.index(nums[indx])]
            ans.append(len(temp))
        
        return ans

