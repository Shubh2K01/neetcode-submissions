class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = []
        for n in nums:
            prefix.append(pre)
            pre *= n
        
        postfix = [1] * len(nums)
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = post
            post *= nums[i]
            
        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])

        return output
        