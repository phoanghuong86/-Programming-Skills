class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []

        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i]+1])
            if len(arr) >= 2 and all(arr[i] - arr[i-1] == arr[1] - arr[0] for i in range(1,len(arr))):
                res.append(True)
            else:
                res.append(False)

        return res
