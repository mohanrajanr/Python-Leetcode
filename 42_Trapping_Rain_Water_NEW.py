# # # # -*- coding: utf-8 -*-
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0

        water_result = 0
        max_left = []
        max_val = 0
        # 对height来说,维护每个元素(不包含当前元素)左边最大的值
        for i in range(0,len(height)):
            max_left.insert(i,max_val)
            max_val = max(height[i],max_val)
        max_val = 0

        for i in range(len(height)-1,-1,-1):
            max_val = max(height[i],max_val)
            #
            lowest_left_right = min(max_left[i],max_val)
            water_result += lowest_left_right - height[i] if lowest_left_right > height[i] else 0
        #print max_left
        return water_result

if __name__ == '__main__':
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print s.trap(height)

