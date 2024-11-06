class Solution:
    def maxArea(self, height: List[int]) -> int:
        # init two pointers and maxArea.
        front = 0
        back = len(height) - 1
        maxArea = 0
      
        # go until pointers reach each other.
        while front != back:
            # calculate area.
            h = min(height[front], height[back])
            dist = back - front
            area = h * dist
          
            # store if greater than current maxArea.
            if area > maxArea:
                maxArea = area

            # move pointers.
            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        # return ans.
        return maxArea
                
            
                    
            


            

