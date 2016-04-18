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
        height.append(0)

        curr = 0
        while curr < len(height):

            if height[curr+1] > height[curr]:
                curr += 1
                continue
            #The next val is smaller than curr_val, then we can search for a high
            curr_val = height[curr]

            i = curr + 2

            while i < len(height) - 1:
                i_val = height[i]
                # Attention to this index!
                max_val = max(height[curr+1:i]) # This is the max value between curr and i

                #当找到的curr比curr-1大,且i比i+i大时
                if curr_val >= max_val and i_val >= max_val and (height[i] > height[i+1]):
                    low = min(i_val,curr_val)
                    high_position = i
                    for j in range(curr+1,high_position):
                        diff = low - height[j]
                        water_result += diff
                    #此次运算完成,退出当前i的循环,跳回curr
                    break
                else:
                    i += 1

            curr = i

            if curr >= len(height) - 2:
                return water_result

        return water_result

if __name__ == '__main__':
    s = Solution()
    height = [1,1,1]
    print s.trap(height)