class Solution:

    def encode(self, strs: List[str]) -> str:
        word = 'å'
        for string in strs:
            word += string + 'å'
        return word

    def decode(self, s: str) -> List[str]:
        strings = []
        word = ""
        for char in s:
            if char == 'å':
                strings.append(word)
                word = ""
                continue
            else:
                word += char
        strings.remove("")
        return strings