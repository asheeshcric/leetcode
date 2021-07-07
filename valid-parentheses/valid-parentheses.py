class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []
        paran_map = {"(": ")", "{": "}", "[": "]"}
        for paran in s:
            if paran in ["(", "{", "["]:
                stack.append(paran)
            elif len(stack) > 0:
                last_paran = stack.pop()
                if paran_map[last_paran] != paran:
                    return False
            else:
                return False

        return True if len(stack) == 0 else False