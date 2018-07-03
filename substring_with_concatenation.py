from itertools import combinations, combinations_with_replacement
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        hist, n = {}, len(words[0])
        for word in words:
            if word not in hist:
                hist[word] = 0
            hist[word] += 1

        
        print(hist[word])

        


sol = Solution()

s = "barfoothefoobarman"
words = ["foo","bar"]
sol.findSubstring(s,words)

