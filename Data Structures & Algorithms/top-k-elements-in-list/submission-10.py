class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        cl=sorted(c.items(),key=lambda x:x[1],reverse =True)
        sorted_counts=dict(cl[:k])
        return [i for i in sorted_counts]