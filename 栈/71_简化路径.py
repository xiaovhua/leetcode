# 列表转字符串的用法：''.join(path) 表示用 '' 将列表 path 的元素连接起来，'/'.join(path) 则表示列表元素间用 '/' 连接
# 多使用 if a，a 直接是各种基本类型的非空或空数据，而不一定要 bool
class Solution(object):
    def simplifyPath(self, path):
        path_list = str.split(str(path), '/')
        new_path = ['/']
        print(path_list)
        for ch in path_list:
            if ch == '.' or ch == '':
                pass
            elif ch == '..':
                try:
                    new_path.pop()
                except:
                    pass
            else:
                new_path.append(ch + '/')
        new_path = ''.join(new_path)
        if len(new_path) <= 1:
            return '/'
        else:
            if new_path[-1] == '/':
                new_path = new_path[:-1]
            if new_path[0] != '/':
                new_path = '/' + new_path
        return new_path

    def simplifyPath2(self, path):
        path_list = path.split('/')
        new_path = []
        for ch in path_list:
            if ch == '..':
                if new_path:
                    new_path.pop()
            elif ch and ch != '.':
                new_path.append(ch)
        print(new_path)
        print('/'.join(new_path))
        return '/' + '/'.join(new_path)

solution = Solution()
print(solution.simplifyPath2("/home/../../.."))