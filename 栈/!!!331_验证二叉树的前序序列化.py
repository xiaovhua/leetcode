"""
给定一个前序序列化表示的树，其终端节点用 # 代替，判断其是否为完全二叉树
"""
class Solution(object):
    def isValidSerialization(self, preorder):
        pre_list = str.split(str(preorder), ',')
        dif = 1
        for i in range(len(pre_list)):
            if pre_list[i] != '#':
                dif += 2
            dif -= 1
            if dif < 0:
                return False
            if dif == 0 and i != len(pre_list) - 1:
                return False
        if dif == 0:
            return True
        else:
            return False

    # 改进版：先 -1 判断是否满足 dif >= 0 的条件
    def isValidSerialization2(self, preorder):
        pre_list = str.split(str(preorder), ',')
        dif = 1
        for i in range(len(pre_list)):
            dif -= 1
            if dif < 0:
                return False
            if pre_list[i] != '#':
                dif += 2
        return dif == 0

solution = Solution()
print(solution.isValidSerialization2("1,#,#,1"))


