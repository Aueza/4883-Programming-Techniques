class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # If the last digit is not a 9, increment by 1.
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        # If the last digit is not a 9.
        else:
            index = -1
            # Traverse the reversal of the list.
            for num in reversed(digits):
                # If the list is full of 9's. Replace them with a 0 and insert 1 to the front.
                if num == 9 and num == digits[0] and abs(0 - index) == len(digits):
                    digits[index] = 0
                    digits.insert(0, 1)
                    return digits
                # If the number is a 9 and not at the front. Replace with a 0.
                elif num == 9:
                    digits[index] = 0
                # If the number is not a 9. Increment by 1.
                elif num != 9:
                    digits[index] += 1
                    return digits
                index -= 1
