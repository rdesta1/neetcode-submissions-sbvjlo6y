# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortExtra(pairs, 0, len(pairs) - 1)
        return pairs
        
    def quickSortExtra(self, pairs: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return
            
        pivot = pairs[e].key
        left = s
        
        for i in range(s, e):
            if pairs[i].key < pivot:
                tmp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = tmp
                left += 1

        pairs[e], pairs[left] = pairs[left], pairs[e]

        self.quickSortExtra(pairs, s, left-1)

        self.quickSortExtra(pairs, left + 1, e)
