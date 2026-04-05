class Solution:

    def encode(self, strs: List[str]) -> str:
        newList = ""
        for i in strs:
            length = len(i)
            newList += str(length) + ":" + i
        return newList

    def decode(self, s: str) -> List[str]:
        newArray = []
        i = 0
        while i < len(s):
            colon_pos = s.find(":", i)      # finds : starting at position i
            length_str = s[i:colon_pos]     # gets number before colon
            length = int(length_str)        # converts to int
            i = colon_pos+1                 # moves i to right after the colon
            eachstring = s[i:i + length]    # gets string from i to (i+length)
            newArray.append(eachstring)     # appends new string to array
            i+= length                      # puts i at next number
        return newArray

