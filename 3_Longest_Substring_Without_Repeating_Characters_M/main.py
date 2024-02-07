def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 2: return len(s)

    mySet = set()
    L, R = 0, 0
    maxLength = 0
    for i in range(len(s)):
        if ord(s[R]) in mySet:
            while ord(s[R]) in mySet:
                mySet.remove(ord(s[L]))
                L += 1

        mySet.add(ord(s[R]))
        maxLength = max(maxLength, R - L + 1)
        R += 1

    return maxLength

# print(lengthOfLongestSubstring('abcabcbb'))