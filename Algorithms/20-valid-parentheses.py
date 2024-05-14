class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) < 2:
            return False

        currentOpen = []

        lst = list(s)
        for c in lst:
            if c in '([{':
                currentOpen.append(c)
            # Closing parentheses
            else:
                if not currentOpen or \
                    (c == ')' and currentOpen[-1] != '(') or \
                    (c == '}' and currentOpen[-1] != '{') or \
                    (c == ']' and currentOpen[-1] != '['):
                    return False
                currentOpen.pop()
        return not currentOpen


    print(isValid("){"))
        