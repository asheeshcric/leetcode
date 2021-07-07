class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1 or len(s) <= k:
            return len(s)

        # Start the window from the leftmost char with window_size as 1
        left, right = 0, 0
        seen_chars = dict()
        max_len = 1
        while right < len(s) and left < len(s):
            # Right pointer is going to move anyway, so add the new letter to the dictionary
            if s[right] in seen_chars:
                seen_chars[s[right]] += 1
            else:
                seen_chars[s[right]] = 1
            
            window_size = right - left + 1
            if window_size - max(seen_chars.values()) <= k:
                # This means we can make all chars same in the substring with k or less operations
                max_len = max(max_len, window_size)
                right += 1
            else:
                # First, remove the count of the left letter from the dictionary
                if s[left] in seen_chars:
                    seen_chars[s[left]] -= 1
                left += 1
                right += 1


        return max_len