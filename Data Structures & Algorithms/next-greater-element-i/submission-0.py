class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        greater = {}
        stack = []
        result = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                greater[stack.pop()] = num
            stack.append(num)

        while stack:
            greater[stack.pop()] = -1
        
        result = [greater[num] for num in nums1]

        return result