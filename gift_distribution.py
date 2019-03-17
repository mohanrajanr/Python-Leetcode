# DFS
class Solution:
    def permute(self, nums):
        res = []
        result = []
        self.dfs(nums, [], res)
        for r in res:
            if self.validateIndex(r):
                result.append(r)
        return result

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            next_nums = nums[:i] + nums[i+1:]
            self.dfs(next_nums, path + [nums[i]], res)

    def validateIndex(self, array):
        for i in range(len(array)):
            if array[i] == i:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [0,1,2,3]
    print(s.permute(nums))