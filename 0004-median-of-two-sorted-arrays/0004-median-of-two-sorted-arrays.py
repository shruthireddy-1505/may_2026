class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        def merge(arr):
            if len(arr)>1:
                left = arr[:len(arr)//2]
                right = arr[len(arr)//2:]

                merge(left)
                merge(right)

                i = 0
                j = 0
                k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1 
                    k += 1
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
        merge(arr)
        n = len(arr)
        if n % 2 != 0:
            return arr[n // 2]
        return (arr[n // 2] + arr[(n // 2) - 1]) / 2
        