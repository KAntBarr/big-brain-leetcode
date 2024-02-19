class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '' or s == ' ': return True

        filteredString = ''.join(char for char in s if char.isalnum()).lower()

        L = 0
        R = len(filteredString) - 1
        while L <= R:
            if not filteredString[L] == filteredString[R]:
                return False
            L += 1
            R -= 1
        
        return True