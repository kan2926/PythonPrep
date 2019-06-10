# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:46:39 2019

@author: kanyad
"""


#def kill_process(pid, ppid, kill):

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        @solution: hashmap + dfs
        @runtime:  400ms
        @timecomplexity: O(n)
        """
        ret = []
        hm = dict()
        for i in range(len(ppid)):
            print('i',i)
            print('hm', hm)
            group = hm.setdefault(ppid[i], [])
            print('group---',group)
            group.append(pid[i])
            print('group---',group)
        print(group)
        print(hm)
        self.dfs(hm, kill, ret)
        return ret
    
    def dfs(self, hm, node, ret):
        ret.append(node)
        if node in hm:
            
            for child in hm.get(node):
                print('child', child)
                self.dfs(hm, child, ret)
                

s = Solution()


class Solution1:
    def kill_process(self, pid, ppid, kill):
        ret = []
        d = dict()
        for i in range(len(ppid)):
            temp = d.setdefault(ppid[i],[])
            temp.append(pid[i])
        self.dfs(d, kill, ret)
        return ret
        
    def dfs(self, d, kill, ret):
        ret.append(kill)
        if kill in d:
            for child in d.get(kill):
                self.dfs(d, child, ret)
        


p = Solution1()
pid = [1,3,10,5,7,6,8, 12,19]
ppid = [3,0,5,3,10,5,10, 6,12]
kill = 5

#print(ppid.count(kill))

#print(pid.__getitem__(ppid.index(kill)))

#print(s.killProcess(pid,ppid, kill))
print(p.kill_process(pid, ppid, kill))