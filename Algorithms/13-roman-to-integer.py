class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        switch ={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        val = 0
        # I conditions
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        for c in s:
            val += switch[c]

        return val

    s = "MCMXCIV"
    print(romanToInt(s))