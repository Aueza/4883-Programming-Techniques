# Maximum Profit in Job Scheduling - Leetcode 1235
Ethan Saenz
## Problem Overview
**Goal**: 
 - Maximize profit by scheduling non-overlapping jobs.

**Given**: 
 - Arrays for startTime, endTime, and profit. 
 - Constraints on overlapping jobs.

**Objective**: 
 - Select jobs with maximum profit without overlap.
## Components to Understand
**Dyanmic Programming**:
 - Using previous computations to build an optimal solution.
 - We will use dp to store the maximum achievable profit up to each job.

**Binary Search**:
 - Find the last job that doesn’t overlap with the current job.
 - Speeds up the process of finding non-overlapping jobs, reducing complexity.
## Methodology
**1.) Sort Jobs**: 
 - Sort by end time to make checking overlapping easier.
   
**2.) Define DP Array**: 
 - dp[i] stores maximum profit up to the i-th job.
   
**3.) Binary Search for Latest Non-Overlapping Job**:
 - For each job i, find the last job j that ends before job i starts.
 - Use the binary search function.

**4.)	Compute DP Array**:  
 - Set dp[i] to the maximum of including or excluding the job.

**5.)	Result**: 
 - dp[-1] gives the maximum profit possible.
## Solution Code
```
from bisect import bisect_right
class Solution:
def jobScheduling(self, startTime: List[int], endTime:		           List[int], profit: List[int]) -> int:

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
```
## Code Explanation
**1.) Sort and Prepare Arrays**: 
 - Jobs are sorted by end times.
 - Dp and end_time arrays are initialized.
   
**2.)Binary Search for Non-Overlapping Jobs**:
 - For each job, find the latest job that doesn’t overlap.

**3.) Calculate DP Values**:
 - Choose max profit between including or excluding each job.
 - Store result in dp[i].

**4.) Return Result**:  
 - dp[-1] holds the maximum achievable profit.
## Complexity Analysis
**Time Complexity**: O(n log n)
 - Sorting is O(n log n)
 - Binary Search for each job is O(log n)

**Space Complexity**: O(n)
 - Storing job data and dp array.
## Summary
**Problem Solved Using**: 
 - Dynamic Programming and Binary Search.
   
**Key Takeaway**:  
 - Efficient job scheduling with max profit by leveraging previous calculations.
   
**Real-World Applications**: 
 - Task scheduling and resource management in operating systems.
   
**Alternatives**: 
 - Priority Queue (Max Heap), Map, or Dictionary instead of sorting or binary search.
## Example
![Leetcode1235Example](https://github.com/user-attachments/assets/8ef41755-8c01-41a2-8c07-a4a144c09b09)
