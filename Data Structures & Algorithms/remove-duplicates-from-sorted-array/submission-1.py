class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = sorted(set(nums))

        for i in range(len(k)):
            nums[i] = k[i]

        return len(k)