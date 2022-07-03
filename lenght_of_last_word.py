class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = s.split()
        #fin_list = [s.strip() for s in list_s] 
        lenght = len(list_s[-1])
        return lenght




