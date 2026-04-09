class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        
        freq = {}
        need = 0
        
        for c in t:
            freq[c] = 1 + freq.get(c, 0)

        need = len(freq)
        have = 0
        freq_s = {} 
        l = 0
        min_len = float('inf')
        res = [0,0]

        for r in range(len(s)):
            c = s[r]
            freq_s[c] = 1 + freq_s.get(c, 0)
            if c in freq and freq_s[c] == freq[c]:
                have += 1

            
            while have == need:
                if (r - l + 1) < min_len:
                    res = [l, r]
                    min_len = r - l + 1
                
                freq_s[s[l]] -= 1
                if s[l] in freq and freq_s[s[l]] < freq[s[l]]:
                    have -= 1
                l+=1

        if min_len == float('inf'):
            return ""
        else:
            l, r = res
            return s[l:r+1]


        


                    
        