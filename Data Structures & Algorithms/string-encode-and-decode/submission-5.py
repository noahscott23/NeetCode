class Solution:
    def encode(self, strs: List[str]) -> str:
        retStr = ""
        for i in strs:
            length = len(i)
            retStr += str(length) + "!" + i
        return retStr


    def decode(self, s: str) -> List[str]:
        newList = []
        i = 0
        while i < len(s):
            position = s.find("!", i)
            length = int(s[i:position])
            i = position+1
            string = s[i:i+length]
            newList.append(string)
            i += length
        return newList

