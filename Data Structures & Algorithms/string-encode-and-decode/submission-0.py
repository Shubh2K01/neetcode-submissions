class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            s_length = ""
            while s[i] != "#":
                s_length += s[i]
                i += 1
            s_length = int(s_length)
            word = ""
            for j in range(i + 1, i + s_length + 1):
                word += s[j]
            res.append(word)
            i += s_length + 1
        return res