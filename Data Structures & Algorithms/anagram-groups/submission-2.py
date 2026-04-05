class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for i in strs:
            char_count = [0] * 26
            for char in i:
                char_count[ord(char)- ord('a')] += 1
            ans[tuple(char_count)].append(i)

        return list(ans.values())

        