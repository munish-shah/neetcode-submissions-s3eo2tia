class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            #george
            #eoregg
        hashtable_s = {}
        hashtable_t = {}
        for i in range(len(s)):
            hashtable_s[s[i]] = 1 + hashtable_s.get(s[i],0)
            hashtable_t[t[i]] = 1 + hashtable_t.get(t[i],0)
        for x in hashtable_s:
            if x not in hashtable_t:
                return False
            if hashtable_s[x] != hashtable_t[x]:
                return False
        return True
