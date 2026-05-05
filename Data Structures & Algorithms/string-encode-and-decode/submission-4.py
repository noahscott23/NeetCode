class Solution:
    def encode(self, strs: List[str]) -> str:
        returnStr = ""
        for i in strs:
            length = len(i)
            returnStr += str(length) + ":" + i
        return returnStr

    def decode(self, s: str) -> List[str]:
        newList = []
        i = 0
        while (i < len(s)):
            colon_pos = s.find(":", i)
            length = int(s[i:colon_pos])
            i = colon_pos+1
            string = s[i:i+length]
            newList.append(string)

            i += length
        return newList

