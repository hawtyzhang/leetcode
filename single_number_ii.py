class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        freq = [0 for i in range(32)]
        sign = 0
        for i in A:
            if i < 0:
                sign += 1
            for digit in range(32):
                if i % 2 != 0:
                    freq[digit] += 1
                i /= 2
        result = 0
        for digit in range(32):
            if freq[digit] % 3 != 0:
                result += 2**digit
        if sign % 3 != 0:
            result += -2**32
        return result
