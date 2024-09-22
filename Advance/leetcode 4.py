class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        merged_array = sorted(nums1)
        if len(merged_array) % 2 == 0:
            first_num = len(merged_array) // 2
            second_num = first_num - 1
            result = (merged_array[first_num] + merged_array[second_num]) / 2
        else:
            num = len(merged_array) // 2
            result = merged_array[num]
        return result

sol = Solution()

nums1 = [1, 2]
nums2 = [3,4]
result = sol.findMedianSortedArrays(nums1, nums2)

print("Median of the merged sorted arrays:", result)
