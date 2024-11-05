class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # cast int to a string
        s1 = str(x)

        # init two pointers to front and back
        front = 0
        back = len(s1) - 1

        # check for matching chars then move towards middle.
        for c in s1:
            if(s1[front] == s1[back]):
                front += 1
                back -= 1
            else:
                return False
        return True

