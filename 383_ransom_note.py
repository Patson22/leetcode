class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        """
        x = list(ransomNote)
        x.sort
        y = list(magazine)
        y.sort
        """
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, '', 1)
            else:
                return False
        return True
