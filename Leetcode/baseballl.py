class Solution:
    def calPoints(self, arr: list[str]) -> int:
        stack = []
        for a in arr:
            if a == "D":
                stack.append(int(stack[-1]) * 2)
            elif a == "C":
                stack.pop()
            elif a == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(int(a))
        return sum(stack)
