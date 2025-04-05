class Solution(object):


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num 
            if comp in hashmap:
                return [hashmap[comp],i]

            hashmap[num] = i 

        