class Solution:
    def maxArea(self, nums: List[int]) -> int:
        area=0
        maxarea=0
        l=0
        r=len(nums)-1
        while(l<r):
            length=min(nums[l],nums[r])
            area=length*(r-l)
            maxarea=max(area,maxarea)
            if nums[l]>nums[r]:
                r-=1
            else:
                l+=1
        return maxarea

        