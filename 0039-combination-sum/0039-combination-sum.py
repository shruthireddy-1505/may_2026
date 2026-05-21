class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(ind,nums,target):
            if target == 0:
                res.append(nums[:])
                return
            if ind >= len(arr) or target < 0:
                return 
            nums.append(arr[ind])
            solve(ind,nums,target-arr[ind])

            nums.pop()
            solve(ind+1,nums,target)

        solve(0,[],target)
        return res