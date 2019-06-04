class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = []
        for i in bin(num)[2:]:
            if i == '1':
                res.append(str('0'))
            else:
                res.append(str('1'))
            
        return int(''.join(res),2)