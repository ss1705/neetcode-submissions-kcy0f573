class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # create a dictionary named last, mapping each char to their last index
        # use a start and end pointer to traverse through the string
        # end = max(end, last[s[i]])
        # length of partition = end - start + 1, move start to i+1
        last = {}
        result = []
        start, end = 0, 0

        for i, ch in enumerate(s):
            last[ch] = i

        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(end - start + 1)
                start = i+1

        return result