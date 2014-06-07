class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        rest = [0]
        for i in range(len(gas)):
            rest.append(rest[-1]+gas[i]-cost[i])
        return rest.index(min(rest))
