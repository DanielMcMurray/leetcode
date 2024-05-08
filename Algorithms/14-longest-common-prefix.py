class Solution(object):
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        import os
        return os.path.commonprefix(strs)
    
    print(longestCommonPrefix(["dog","racecar","car"]))