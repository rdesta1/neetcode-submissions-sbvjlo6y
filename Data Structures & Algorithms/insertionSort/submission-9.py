# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sorts = []
        sorts.append(pairs.copy())
        for i in range(1, len(pairs)):
            j = i - 1
            
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                temp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = temp
                j -= 1
            sorts.append(pairs.copy())
        return sorts if sorts != [[]] else []

