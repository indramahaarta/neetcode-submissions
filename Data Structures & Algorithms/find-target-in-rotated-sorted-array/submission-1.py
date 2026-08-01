class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        3,4,5,6,1,2
        L R
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            # print(nums[l], nums[mid], nums[r])
            if target == nums[mid]:
                return mid
            elif nums[l] <= nums[r]:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] >= nums[l]:
                    if target >= nums[l] and target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if target <= nums[r] and target > nums[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
            
        return -1

                

        