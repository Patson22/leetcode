class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num/2)
        elif num == 1:
            return 1
        else:
            return 1 + self.numberOfSteps(num-1)


"""
        steps = 0
        while num > 0:
            if num % 2 == 0:
                steps += 1
                num = num/2
            else:
                num = num-1
                steps += 1
        return (steps)
"""

"""
        n = num

        def calc(n):
            if n == 1:
                return 1
            elif n % 2 == 0:
                return 1 + calc(n/2)
            else:
                return 1 + calc(n-1)
        return calc(num)
"""
