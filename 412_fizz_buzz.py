class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1
        result = []
        while i <= n:
            if (i % 3 == 0) and (i % 5 == 0):
                result.append("FizzBuzz")
                i += 1
            elif i % 3 == 0:
                result.append("Fizz")
                i += 1
            elif i % 5 == 0:
                result.append("Buzz")
                i += 1
            else:
                result.append(str(i))
                i += 1
        return result
