import random
class Solution_demo:
    def randomized_partition(self, nums, l, r): # 随机选择中间点对 nums 从 l 到 r 排序
        pivot = random.randint(l, r) # 选择比较点 pivot，比它小的左边比它大的右边，pivot 含 l 和 r
        nums[pivot], nums[r] = nums[r], nums[pivot] # 统一将 pivot 移到最右边
        i = l - 1 # index 为左标记，放小于比较值 pivot 的数字
        for j in range(l, r): # 遍历用标记
            if nums[j] < nums[r]: # 当发现该点小于比较点 pivot 的值时，塞到最左边，左边的标记位置 +1 并继续
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1 # 结束遍历，小于比较点 pivot 的值全部在 i 左边，i+1 为中间点且将中间点换回来
        nums[i], nums[r] = nums[r], nums[i]
        return i  # 返回中间点的位置

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0: # 结束条件：只有一个人数字在列表中
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    # ————————————————————————————————————————  堆排序  —————————————————————————————————————————————
    def max_heapify(self, heap, root, heap_len): # heapify：调整一个完全二叉树，使其成为最大堆
        p = root # 根节点
        while p * 2 + 1 < heap_len: # 父节点是 p 时，其左右子节点为 2p+1 与 2p+2，父节点是 int((p-1)/2)，int 为下取整
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]: # 只有左节点，或左节点比右节点更大时，记录左节点
                nex = l
            else: # 有右节点且右节点更大时，记录右节点
                nex = r
            if heap[p] < heap[nex]: # 若最大的节点比父节点更大，则交换父节点与该节点
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex # 如果产生了交换使得子节点发生了改变，则要以新的子节点为父节点，对其底下的子节点 heapify
            else:
                break

    def build_heap(self, heap): # 建最大堆：1. 完全二叉树（节点生成顺序从上往下，从左往右） 2. 父节点 > 子节点 (heapify)
        for i in range(len(heap) - 1, -1, -1): # 从 len(heap)-1，逐个 -1 直至 -1（右边为 -1 即最后为 0）
            # 注意，heapify 应该从下往上做，因为如果从上做子节点可能会再改变
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1): # 从下往上，因为是最大堆最小的在最后
            nums[i], nums[0] = nums[0], nums[i] # ——————————注意：因为是最大堆所以要先把最大的输出并放在最后，最后从顶开始输出——————————-
            self.max_heapify(nums, 0, i) # 交换后要重新 heapify

    # ————————————————————————————————————————  归并排序  —————————————————————————————————————————————
    """
    归并排序利用了分治的思想，对一个长为 n 的待排序的序列将其分解成两个长度为 n/2 的子序列，每次先递归调用函数使两个子序列有序，然后再线性合并两个有序的子序列
    """
    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1 # 分治法，将数组分左右两个子数组。左数组 从 l 开始，右数组从中间 mid+1 开始
        while i <= mid or j <= r: # 当左右数组都结束（i 超过 mid 且 j 超过 r）结束
            if i > mid or (j <= r and nums[j] < nums[i]): # 当 i 已经完了右数组的当前值较小，赋值
                tmp.append(nums[j])
                j += 1
            else: # 当 j 已经完了或者左数组的当前值较小
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp # 令从 l 到 r 赋值为 tmp


    def sortArray(self, nums):
        self.merge_sort(nums, 0, len(nums)-1)
        return nums

class MySolution():
    # 快排
    def partition(self, nums, l, r):
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l
        for j in range(l, r):
            if nums[j] < nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def quicksort(self, nums, l, r):
        if l >= r: # 注意：这里要用 >= 而不是 == 因为可能会 l = r + 1（当 pivot = r 时）
            return
        pivot = self.partition(nums, l, r)
        self.quicksort(nums, l, pivot)
        self.quicksort(nums, pivot+1, r)

    # 堆排
    def heapify(self, heap, root, heap_len): # root 和 heap_len 相当于 l 和 r
        p = root
        while 2 * p + 1 <= heap_len:
            l, r = 2 * p + 1, 2 * p + 2
            if r <= heap_len and heap[l] < heap[r]:
                max_child = r
            else:
                max_child = l
            if heap[p] < heap[max_child]:
                heap[max_child], heap[p] = heap[p], heap[max_child]
                p = max_child # 注意，若发生改变要对其子节点作 heapify，不要重新建堆
            else:
                break

    def build_heap(self, nums):
        for i in range((len(nums)-1)//2, -1, -1):
            self.heapify(nums, i, len(nums)-1)

    def heapsort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums)-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i-1)

    # 归并排
    def merge_sort(self, nums, l, r):
        if l >= r:
            return
        mid = (r+l) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid+1, r)
        i, j = l, mid+1
        tmp = []
        while i <= mid or j <= r:
            if j > r or (i <= mid and nums[i] <= nums[j]): # 注意这里的条件语句的逻辑，尤其是 <=，如果等号放下面则非稳定
                tmp.append(nums[i])
                i += 1
            elif i > mid or (j <= r and nums[j] < nums[i]):  # 注意这里的条件语句的逻辑, 也可以用 else
                tmp.append(nums[j])
                j += 1
        nums[l:r+1] = tmp # 不要漏了这句

    # 冒泡：每一轮把最大的数字冒泡到最后面
    def bubble_sort(self, nums):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]



sort = MySolution()
nums = [9, 6, 7, 8, 9, 2, 5, 4, 6, 2, 1, 6, 3, 3, 5, 1, 0]
sort.heapsort(nums)
print(nums)


"""
排序算法总结：
             平均       最坏       最好       空间复杂度         稳定性
插入排序    O(n^2)     O(n^2)      O(n)          O(1)             稳定
希尔排序    O(n^1.3)   ——————     ———————        O(1)             不稳定
冒泡排序    O(n^2)     O(n^2)      O(n)          O(1)             稳定
快速排序    O(nlogn)   O(n^2)      O(nlogn)      O(logn)          不稳定
选择排序    O(n^2)     O(n^2)      O(n^2)        O(1)             不稳定
堆排序      O(nlogn)   O(nlogn)    O(nlogn)      O(1)             不稳定
归并排序    O(nlogn)   O(nlogn)    O(nlogn)      O(n)             稳定
基数排序    O(d(n+r))  O(d(n+r))   O(d(n+r))     O(r)             稳定
1、稳定性：待排序列存在多个相等的数值（但是其他信息不一样，如分数相等但是属于不同的人），排序后对于这些相等的值若其仍然和原顺序同则稳定。
2、复杂度：用比较次数计算
常规遍历：n + (n - 1) + ... 1 = n*(n+1)/2    ->    O(n^2)
二分法： n 不断二分直至分为 1，即以 2 为底 n 的对数，即 logn，若要 5 次才能得到一半则为 5logn。
堆排序：建堆的复杂度为 O(n)，每次踢出元素后调整堆(heapify)的复杂度为 O(nlogn)，踢出 n 个则为 O(nlogn)，总复杂度为 O(n + nlogn) -> O(nlogn)
空间复杂度：快排主要是递归造成的栈空间的使用，最好情况，递归树的深度为 logn，其空间复杂度也就为 O(logn)。归并空间复杂度主要是临时数组，长度为 n。
3、range 的三种用法：
range(5)：从 0 到 4
range(4, 7)：从 4 到 6
range(4, 0, -2)：从 4 到 1 每次 -2
4、最坏情况：
快排：选择最左边为 pivot 点且原数据有序，退化为冒泡（即 pivot 点选得不好，是最大/最小）
冒泡：原数据由大到小（逆序）
5、为什么堆排序没有快排快
第一、堆排序访问数据的方式没有快速排序友好。对于快速排序来说数据是顺序访问的，而对于堆排序来说数据是跳着访问的（叶节点是 2*p + 1）
第二、对于同样的数据，在排序过程中，堆排序算法的数据交换次数要多于快速排序。堆排序的建堆过程会打乱数据原有的相对选择顺序，导致数据有序度降低。比如对于一组已经有序的数据来说，经过建堆之后，数据反而变得更无序了。
"""
