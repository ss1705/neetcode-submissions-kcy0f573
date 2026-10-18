class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        strmap = {}
        seen = set()

        for s_char, t_char in zip(s, t):
            if s_char not in strmap and t_char not in seen:
                strmap[s_char] = t_char
                seen.add(t_char)

            elif s_char not in strmap and t_char in seen:
                return False

            elif s_char in strmap and strmap[s_char] != t_char:
                return False

        return True        