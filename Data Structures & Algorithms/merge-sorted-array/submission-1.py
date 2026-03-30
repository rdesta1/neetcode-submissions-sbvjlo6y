class Solution:
    def mergesort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        #beräkna mitten
        m = (s + e) // 2

        #sortera vänstra delen
        self.mergesort(arr, s, m)
        #sortera högra delen
        self.mergesort(arr, m + 1, e)
        #sammanfoga vänster och höger
        self.mrg(arr, s, m, e)

        return arr 
    
    def mrg(self, arr, s, m, e):
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        #index för L och R
        i, j = 0, 0
        #index för arr
        k = s

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]

        self.mergesort(nums1, 0, m + n - 1)
        
    
 