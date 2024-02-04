class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1: return [strs]

        returnHolder = []
        for word in strs:
            tempDict = {}
            for letter in word:
                if tempDict.get(letter, 0) == 0:
                    tempDict[letter] = 1
                else:
                    tempDict[letter] += 1

            if len(returnHolder) == 0: returnHolder.append({'wordSet': tempDict, 'wordArray': [word]})
            else:
                flag = 1
                for result in returnHolder:
                    if tempDict == result['wordSet']:
                        result['wordArray'].append(word)
                        flag = 0
                        break
                if flag:
                    returnHolder.append({'wordSet': tempDict, 'wordArray': [word]})

            
       
        print(returnHolder)
        returnContainer = []
        for result in returnHolder:
            # print(result)
            returnContainer.append(result['wordArray'])


        return returnContainer