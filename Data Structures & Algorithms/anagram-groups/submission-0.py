class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs: #["act","pots","tops","cat","stop","hat"]
            count = [0] * 26 #[0,0,0,0,0,0,0,0,0,0]
            for letter in word: #["a","c","t"]
                count[ord(letter) - ord('a')] += 1
            # print(count)
            res[tuple(count)].append(word)
        return list(res.values())
            