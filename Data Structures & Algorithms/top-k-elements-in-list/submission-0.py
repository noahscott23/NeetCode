class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int) 
        res = []

        
        for i in nums:  
            a[i] += 1  
        
        while k > 0:
            maximum = max(a, key=a.get)  
            res.append(maximum)
            del a[maximum]  
            k -= 1  

        return res