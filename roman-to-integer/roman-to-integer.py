class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1,
        }
        total = 0
        i = 0
        while i < len(s):
            # If atleast two symbols remaining and current one is less than next one
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                total += roman_map[s[i+1]] - roman_map[s[i]]
                i += 2
            else:
                total += roman_map[s[i]]
                i += 1
        return total
                