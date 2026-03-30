class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            count = 26 * [0]
            for c in string:
                count[ord(c) - ord('a')] += 1
            if tuple(count) in anagrams:
                anagrams[tuple(count)].append(string)
            else:
                anagrams[tuple(count)] = [string]
        return list(anagrams.values())