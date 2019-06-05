# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:42:37 2019

@author: kanyad
"""
import collections
def findDuplicate(paths):
    dic = collections.defaultdict(list)
    #dic=dict()
    for path in paths:
        root, *f = path.split(" ")
        print('f---',f)
        for file in f:
            txt, content = file.split("(")
            print('txt---',txt)
            dic[content] += root + "/" + txt,
            #tmp = root + "/" + txt
            #dic[content] = dic.get(content,[])+ [tmp]
    #return [dic[key] for key in dic if len(dic[key]) > 1]
    res = []
    for k,v in dic.items():
        if len(v)>1:
            res.append(v)
    return res            
        



inp = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
print(findDuplicate(inp))