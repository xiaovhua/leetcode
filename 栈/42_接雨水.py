# 放弃
class Solution(object):
# 思路：对每个下标 i，其上方的接水量是 0, ..., i-1 的最大值和 i+1, ..., n 的最大值的差，可以遍历所有 i（耗时），避免重复计算，采用两个数组：maxleft 和 maxright 来记录每个下标左右两边的最大值，双边循环
    def trap2(self, height):
        if len(height) < 3:
            return 0
        n = len(height)
        area = 0
        maxleft, maxright = [0] * n, [0] * n
        maxleft[0] = 0
        maxright[-1] = 0
        for i in range(1, n):
            maxleft[i] = max(height[i-1], maxleft[i-1])
        for i in range(n-2, -1, -1):
            maxright[i] = max(height[i+1], maxright[i+1])
        for i in range(n):
            if min(maxright[i], maxleft[i]) > height[i]:
                area += min(maxright[i], maxleft[i]) - height[i]
        return area

s = Solution()
print(s.trap2([5,2,1,2,1,5]))
