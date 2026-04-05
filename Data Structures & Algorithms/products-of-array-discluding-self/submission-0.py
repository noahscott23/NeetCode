class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            skip = 0
            product = 1
            first_half = nums[:i]
            second_half = nums[i+1:]
            for j in first_half:
                product = product*j
            for k in second_half:
                product = product*k
            output.append(product)
        return output