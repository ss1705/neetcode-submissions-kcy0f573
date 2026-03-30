class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #use two pointers initialized to two ends of the list
        l, r = 0, len(heights)-1
        res = 0

        #l has to stay to the left of r always
        while l<r:
            #area = width * height
            #width = the distance between the indices of the bars => r-l
            #height = the shortest of the two heights => min(heights[l],heights[r])
            area = (r-l) * min(heights[l],heights[r])
            res = max(area,res)

            #whichever bar has the smaller height should be moved
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res