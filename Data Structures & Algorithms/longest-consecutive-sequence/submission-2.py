class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hash_set = set(nums)
        best = 0

        for i in hash_set:
            if i-1 not in hash_set:
                current_length = 1
                n=i
                while n+1 in hash_set:
                    n += 1
                    current_length += 1
                best = max(current_length, best)
        return best
            
            
