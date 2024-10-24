# My methodology for this was using a double pointer method starting at the front and the back and 
# moving them towards the middle of the list. This could be further optimized by accomplishing this just within
# one pass through the list rather than two. Also, maybe stopping the comparisions when they are at the middle.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize a clean list to store chars
        cleanList = []
        back = -1
        for ch in s:
            # if char is alphabet or number add to cleanList
            if ch.isalpha() or ch.isdigit():
                cleanList.append(ch.lower())
        # iterate over chars in clean list
        for ch in cleanList:
            # double pointer methodology working forwards and backwards checking for equality.
            if ch == cleanList[back]:
                back -= 1
            else:
                return False
        return True
