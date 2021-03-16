class Solution:
    
    def countSubstrings(self, s: str) -> int:
        length, count = len(s), 0
        
        # Loop through each "char" in the string considering them as the center point of the palindrome (if exists)
        # "left_idx" keeps expanding to the left of the center char
        #  "right_idx" keeps expanding to the right of the center char
        # Keep expanding only if the left and right chars match, else move to next char as center point
        # We need to take care of single char palindrome, hence (i, i)
        # We also need to take care of two char palindrom, hence (i, i+1)
        # At the end, if the difference between right_idx and left_idx is greater than 0, then we have found a palindrome 
        
        for i in range(length):
            for left_idx, right_idx in [(i, i),(i, i+1)]:
                while left_idx >= 0 and right_idx < length and s[left_idx] == s[right_idx]:
                    left_idx -= 1
                    right_idx += 1

                count += (right_idx-left_idx) // 2
        return count
        