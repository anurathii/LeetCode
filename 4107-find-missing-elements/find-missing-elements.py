class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        mins, maxs = min(nums), max(nums)
        return [x for x in range(mins, maxs + 1) if x not in s]
     