class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i
            
            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]
            
            # Check if we have the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If the total number of elements is odd
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # If the total number of elements is even
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            
            # If nums1's left part is too big, move i to the left
            elif maxLeft1 > minRight2:
                high = i - 1
            # If nums2's left part is too big, move i to the right
            else:
                low = i + 1
