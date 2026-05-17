class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n-1
        def solve(nums,low,high,target):
            if low > high:
                return -1
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return solve(nums,mid+1,high,target)
            else:
                return solve(nums,low,mid-1,target)

        return solve(nums,l,h,target)
        