class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first = strs[0]

        for i in range(len(first)):
            c = first[i]
            for j in range(len(strs)):
                if (i >= len(strs[j])) or (strs[j][i] != c):
                    return first[:i]

        return first