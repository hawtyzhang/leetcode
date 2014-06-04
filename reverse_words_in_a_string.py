class Solution:
    
    def split(self, string):
        IN, OUT = 0, 1
        state = OUT
        string += ' '
        word_list = []
        word = ''

        for char in string:
            if char != ' ':
                word += char
                state = IN
            else:
                if state == IN:
                    state = OUT
                    word_list.append(word)
                    word = ''
        return word_list

    def join(self, splitter, words):
        result = ''
        for word in words:
            result += word + splitter
        return result[:-len(splitter)]

    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = self.split(s)
        return self.join(" ", words[::-1])

s = Solution()
print s.reverseWords('the sky is blue')
