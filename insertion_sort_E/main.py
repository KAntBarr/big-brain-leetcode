# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) < 2: return [pairs] if len(pairs) else []

        states = [list(pairs)]

        for i in range(1, len(pairs)):
            while pairs[i-1].key > pairs[i].key:
                temp = pairs[i]
                pairs[i] = pairs[i-1]
                pairs[i-1] = temp
                i -= 1
                if i == 0:
                    break
            states.append(list(pairs))
                
        return states