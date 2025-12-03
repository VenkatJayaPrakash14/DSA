class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minV=nums[0]
        ans=0
        for i in range(1,len(nums)):
            ans=max(ans,(nums[i]-minV))
            minV=min(minV,nums[i]) 
        if ans==0:
            ans=-1 
       
        return ans