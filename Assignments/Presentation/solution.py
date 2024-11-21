from bisect import bisect_right
class Solution:
def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

       # sorting jobs into a tuple and init dp, end_times array.
       jobs = sorted(zip(endTime, startTime, profit))
       dp = [0] * (len(jobs) + 1)
       end_times = [job[0] for job in jobs]

       # iterate over jobs.
       for i in range(1, len(jobs) + 1):
           current_end, current_start, current_profit = jobs[i - 1]
           # run binary search.
           j = bisect_right(end_times, current_start)
           # calculate the max profit for that job.
           dp[i] = max(dp[i - 1], dp[j] + current_profit)

       return dp[-1]



