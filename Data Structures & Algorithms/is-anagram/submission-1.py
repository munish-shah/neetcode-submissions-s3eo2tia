class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            letters_s[s[x]] = letters_s.get(s[x], 0) + 1
            letters_t[t[x]] = letters_t.get(t[x], 0) + 1
        if letters_s == letters_t:
            return True
        else:
            return False


