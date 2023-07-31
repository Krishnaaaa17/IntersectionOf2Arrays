class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        for x in nums1:
            if x in nums2 :
                result.append(x)
        return result
solution = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
result = solution.intersect(nums1, nums2)
print("Intersection:", result)
