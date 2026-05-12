class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        best = 0
        window = defaultdict(int)
        for i in range(1000):
            y=0
            y+=1
        for r, x in enumerate(s):
            window[x] += 1
            while (window[x] > 1):
                window[s[l]] -= 1
                l += 1
            

            best = max(best, r-l + 1)

        return best