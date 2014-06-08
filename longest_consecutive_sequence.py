class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        freq = {i:True for i in num}
        longest = 0
        for i in freq:
            if freq[i]:
                consective = 1
                start = i
                while start + 1 in freq:
                    consective += 1
                    start += 1
                    freq[start] = False
                start = i
                while start - 1 in freq:
                    consective += 1
                    start -= 1
                    freq[start] = False

                if longest < consective:
                    longest = consective
        return longest
