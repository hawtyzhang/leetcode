class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candy = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in reversed(range(len(ratings)-1)):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
        return sum(candy)
