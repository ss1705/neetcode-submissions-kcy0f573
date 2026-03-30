class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #initialize left and right pointers for binary search
        #we will consider the range from 1 to the max(piles) which is the piles with the max. bananas
        l, r = 1, max(piles)
        #we are also initializing the result to r because that's the next possible solution for the problem before we compute anything
        res = r

        #start the binary search loop
        while l <= r:
            #set k to the middle of the range
            k = (l+r) // 2
            #initialize hours
            hours = 0
            for p in piles:
                #add the hours required to eat each piles, using ceil to round up to the next integer
                #eg: piles=[3,6,9], k=2 ==> hours = 3/2=2 + 6/2=3 + 9/2=5 ==> hours = 2+3+5 = 10
                hours += math.ceil(p/k)
            
            #if the calculated hours is lesser than the given h, then we update that rate k to be result and also shift the range to perform binary search to find a smaller k if possible
            if hours <= h:
                    res = k
                    r = k-1
            #if not, we shift the range to find a bigger k in order to minimize the time
            else:
                    l = k+1
        
        return res

