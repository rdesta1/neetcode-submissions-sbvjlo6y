class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        k = 0

        while True:
            for wor in strs:
                if k >= len(wor) or strs[0][k] != wor[k]:
                    return prefix
            prefix += strs[0][k]
            k += 1