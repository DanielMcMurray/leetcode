class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)^2
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        # O(n)   
        map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in map:
                return[map[complement], i]
            map[n] = i

    print(twoSum([2,7,11,15], 13))