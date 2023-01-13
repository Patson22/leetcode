class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_num = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rom = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        x = len(s)
        result = 0
        i = 0
        while i != x-1:
            if rom.index(s[i]) < rom.index(s[i+1]):
                result -= roman_num[s[i]]
                i += 1
            else:
                result += roman_num[s[i]]
                i += 1
        result += roman_num[s[i]]
        return (result)
