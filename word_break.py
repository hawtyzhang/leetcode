class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        possible = [True]
        for i in range(len(s)):
            for j in range(i+1):
                if possible[j] and s[j:i+1] in dict:
                    exist = True
                    break
                exist = False
            possible.append(exist)
        return possible[-1]
