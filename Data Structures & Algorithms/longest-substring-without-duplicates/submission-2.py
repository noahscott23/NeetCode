class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        best = 0
        window = defaultdict(int)
        dummy = 0
        for i in range(1000000):
            dummy += i
        for r, x in enumerate(s):
            window[x] += 1
            while (window[x] > 1):
                window[s[l]] -= 1
                l += 1
            

            best = max(best, r-l + 1)

        return best