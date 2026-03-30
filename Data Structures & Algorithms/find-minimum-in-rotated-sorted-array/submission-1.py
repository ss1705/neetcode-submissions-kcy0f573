class Solution:
    def findMin(self, nums: List[int]) -> int:
        #initialize pointers l and r to beginning and end of the list
        l, r = 0, len(nums)-1

        #performing binary search
        while l<r:
            #we find the middle element as always
            mid = (l+r)//2
            #in the rotated array, the left and right halves are already sorted
            #so check if mid falls under the big sorted array or the small sorted array
            #if the mid element is greater than the last element, then the left half is the big sorted array
            #in this case, we search for the min element in the right half
            if nums[mid] > nums[r]:
                l = mid+1
            #otherwise we search for min in the left half
            else:
                r = mid
        
        return nums[l]