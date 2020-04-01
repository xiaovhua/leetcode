class Solution(object):
    def isValid(self, s):
        dict = {'(': ')', '[': ']', '{': '}'}
        need = []
        for ch in s:
            if ch in ['(', '[', '{']:
                need.append(dict[ch])
            elif ch in [')', ']', '}']:
                if len(need) <= 0:
                    return False
                if ch == need[-1]:
                    need.pop()
                else:
                    return False
        return len(need) == 0

solution = Solution()
print(solution.isValid('()'))