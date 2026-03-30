class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {} #this is the hashmap, mapping every number to its index in the list

        for i,num in enumerate(nums): #loop through each number with its index
            comp = target - num #find the remaining value taking the current number as one of the parts
            
            if comp in num_to_index: #check if the rem. value is in the hashmap
                return [num_to_index[comp],i] #return the two indices - num and rem. value's
            
            num_to_index[num]=i #if not found, add the index of the current number

        return [] #edge case