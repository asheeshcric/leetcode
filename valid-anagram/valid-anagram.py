class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or not s or not t:
            return False

        s_counts = self.get_char_counts(s)
        t_counts = self.get_char_counts(t)
        for char, count in s_counts.items():
            if count != t_counts.get(char, 0):
                return False

        return True
    
    def get_char_counts(self, string):
        char_counts = dict()
        for char in string:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

        return char_counts