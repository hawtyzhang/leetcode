class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not self.check(s, dict):
            return []
        possible = [[] for i in range(len(s)+1)]
        possible[0] = [""]
        for i in range(len(s)):
            exist = []
            for j in range(i+1):
                if possible[j] and s[j:i+1] in dict:
                    exist += [k + " " + s[j:i+1] for k in possible[j]]
            possible[i+1] = exist
        return [i[1:] for i in possible[-1]]
    
    def check(self, s, dict):
        possible = [True]
        for i in range(len(s)):
            for j in range(i+1):
                if possible[j] and s[j:i+1] in dict:
                    exist = True
                    break
                exist = False
            possible.append(exist)
        return possible[-1]
        


s = Solution()
a= s.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])
