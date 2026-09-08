class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        #. 4#neet4#code4#love3#you
        res = []
        i = 0
        while(i != len(s)):
            string_length = ""
            while(s[i] != '#'):
                string_length += s[i]
                i += 1
            word = ""
            string_length = int(string_length)
            res.append(s[i + 1: i + 1 + string_length])
            i += string_length + 1
        return res