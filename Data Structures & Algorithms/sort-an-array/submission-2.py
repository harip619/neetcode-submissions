import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l,r):
            if l>=r:
                return
            pi=random.randint(l,r)
            nums[pi],nums[r]=nums[r],nums[pi]
            pivot=nums[r]
            
            i=l
            for j in range(l,r):
                if(nums[j]<pivot):
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
            nums[i],nums[r]=nums[r],nums[i]
            quicksort(l, i - 1)
            quicksort(i + 1, r)

        quicksort(0, len(nums) - 1)
        return nums
