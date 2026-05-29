from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s_count  = Counter(s)
            t_count = Counter(t)
            if len(s_count)!=len(t_count):
                return False
            else:
                for k,v in s_count.items():
                    if k in t_count and v == t_count[k]:
                        continue
                    else:
                        return False
        return True
        