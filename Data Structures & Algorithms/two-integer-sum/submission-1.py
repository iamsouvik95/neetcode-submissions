class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output=[]
        for i in range(0,len(nums)):
            comp=target-nums[i]
            if comp in nums[(i+1):len(nums)]:
                output.append(i)
                output.append(nums.index(comp, i + 1))
                
        return output
        