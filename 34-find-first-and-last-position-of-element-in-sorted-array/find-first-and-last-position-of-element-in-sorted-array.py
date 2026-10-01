class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound(val: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return left

        start = lower_bound(target)
        
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = lower_bound(target + 1) - 1

        return [start, end]