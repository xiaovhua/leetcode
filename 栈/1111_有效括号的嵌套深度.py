class Solution:
    def maxDepthAfterSplit(self, seq):
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        return ans

class MySolution(object):
    def maxDepthAfterSplit(self, seq):
        # N：欠的数量，depth：深度
        a = {'N': 0, 'depth': 0}
        b = {'N': 0, 'depth': 0}
        ans = []
        for c in seq:
            if c == '(':
                if a['depth'] <= b['depth']:
                    ans.append(0)
                    a['depth'] += 1
                    a['N'] -= 1
                else:
                    ans.append(1)
                    b['depth'] += 1
                    b['N'] -= 1
            else:
                if a['N'] < 0:
                    a['N'] += 1
                    a['depth'] -= 1
                    ans.append(0)
                else:
                    b['N'] += 1
                    b['depth'] -= 1
                    ans.append(1)
        return ans

    def maxDepthAfterSplit2(self, seq):
        depth = 0 # 总 depth，保证均匀分给两个序列
        ans = []
        for c in seq:
            if c == "(": # 先给 0，然后为基数则给 1，为偶数则给 0，保证分配均匀
                ans.append(depth%2)
                depth += 1
            else:
                depth -= 1 # 同样的道理，但是要和上面相反：要么上面先加下面后减，要么上面后加下面先减，保证分配给最新添加的'('括号中
                ans.append(depth%2)
        return ans


solution = Solution()
print(solution.maxDepthAfterSplit('()(())'))