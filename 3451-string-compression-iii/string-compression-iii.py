class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while i < len(word):
            current_char = word[i]
            length = 0
            while i + length < len(word) and word[i + length] == current_char and length < 9:
                length += 1
            comp += str(length) + current_char
            i += length
        return comp
