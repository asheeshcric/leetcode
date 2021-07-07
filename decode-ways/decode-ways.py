class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [None] * (len(s) + 1)
        dp[0] = 1
        return self.decode_ways(s, dp, n=1)
    
    def decode_ways(self, s, dp, n):
        if len(s[n - 1 :]) == 0:
            return 1

        if s[n - 1] == "0":
            return 0

        if len(s[n - 1 :]) == 1:
            return 1

        if dp[n] is not None:
            return dp[n]

        if int(s[n - 1]) <= 2 and int(s[n - 1 : n + 1]) <= 26:
            # Two ways to decode
            dp[n] = self.decode_ways(s, dp, n + 1) + self.decode_ways(s, dp, n + 2)
        else:
            # Only one way to decode
            dp[n] = self.decode_ways(s, dp, n + 1)

        return dp[n]
        