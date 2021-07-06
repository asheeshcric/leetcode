class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        
        count, max_count = 0, 0
        for i, char in enumerate(s):
            if char not in seen:
                seen.append(char)
                count += 1
            else:
                # The char has already been seen
                index = seen.index(char)
                # Remove that char from seen and the ones before it
                seen = seen[index+1:] if index+1 < len(seen) else []
                seen.append(char)
                count = len(seen)
                
            max_count = max(max_count, count)
            
        return max_count