class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        if x == x[::-1]:
            return True
        else:
            return False

    isPalindrome(121)