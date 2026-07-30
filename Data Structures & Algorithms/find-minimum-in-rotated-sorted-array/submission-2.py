class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        res = nums[r]
        # ctr = 100
        while l < r:
            # ctr -= 1
            # if ctr ==0:
            #     break
            # print(l, r)
            # print(l, r, res)
            
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            res = min(res,nums[r])
            mid = (l+r)//2
            if nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1
                res = min(res,nums[mid])
            # res = min(nums[r], nums[mid])
        
        return res

        