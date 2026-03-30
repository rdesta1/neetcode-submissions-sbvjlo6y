# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        length = len(pairs) - 1
        
        return self.helper(pairs, 0, length)
        
    def helper(self, arr: list[int], s: int, e: int) -> list[int]:
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        left = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot
        
        # Quick sort left side
        self.helper(arr, s, left - 1)

        # Quick sort right side
        self.helper(arr, left + 1, e)

        return arr