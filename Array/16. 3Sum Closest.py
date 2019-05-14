class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(N^2)
        res = []
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == target:
                    return curr
                if abs(curr - target) < abs(res - target):
                    res = curr
                if curr < target:
                    j += 1
                elif curr > target:
                    k -= 1
        return res