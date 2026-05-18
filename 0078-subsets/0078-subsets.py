class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(ind,arr):
            if ind >= len(nums):
                res.append(arr[:])
                return
            arr.append(nums[ind])
            solve(ind+1,arr)

            arr.pop()
            solve(ind+1,arr)

        solve(0,[])

        return res