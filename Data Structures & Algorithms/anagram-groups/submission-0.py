class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = defaultdict(list)

        for i in strs:
            i_sorted = ''.join(sorted(i))
            amap[i_sorted].append(i)

        return list(amap.values())