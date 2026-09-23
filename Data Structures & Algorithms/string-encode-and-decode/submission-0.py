class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        pointer = 0

        while pointer < len(s):
            hash_idx = s.find("#", pointer)
            length = int(s[pointer:hash_idx])
            content_start = hash_idx+1
            substring = s[content_start:content_start+length]
            result.append(substring)
            pointer = content_start+length
        
        return result