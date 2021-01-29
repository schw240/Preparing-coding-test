class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        plen = len(prefix)

        for s in strs[1:]:
            while prefix != s[0:plen]:
                print(prefix, "up")
                prefix = prefix[0:(plen-1)]
                print(prefix, "down")
                plen -= 1

                if plen == 0:
                    return ""
        return prefix
