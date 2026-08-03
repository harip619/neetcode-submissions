class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        l=0
        for i in nums:
            if(i-1) not in numset:
                le=0
                while(i+le) in numset:
                    le+=1
                l=max(l,le)
        return l