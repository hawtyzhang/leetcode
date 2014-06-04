import operator

class Solution:
    def div_round_to_zero(self, a, b):
        # Leetcode only accept round to zero result
        return a//b if a*b>0 else (a+(-a%b))//b

    def evalRPN(self, tokens):
        # @param tokens, a list of string
        # @return an integer
        operators_map = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : self.div_round_to_zero,
        }
        operators = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i in operators:
                last = stack.pop()
                second = stack.pop()
                stack.append(operators_map[i](second, last))
            else:
                stack.append(int(i))

        return stack[0]

s = Solution()
print s.evalRPN(["2", "1", "+", "3", "*"])
print s.evalRPN(["4", "13", "5", "/", "+"])
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
