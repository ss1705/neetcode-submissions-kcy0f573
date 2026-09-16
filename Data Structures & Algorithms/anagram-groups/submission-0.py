from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_fam = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - ord('a')] += 1

            count_key = tuple(count)
            anagram_fam[count_key].append(string)

        return list(anagram_fam.values())
        