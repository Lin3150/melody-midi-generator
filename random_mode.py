#!/usr/bin/env python
# -*-coding:utf-8 -*-

#根据notelist，生成重音选择表，禁忌表，琶音片段表，random正太音高表
#时长表
import random

def notetime():
    return [60, 120, 120, 120, 240, 240, 240, 240, 480]

def zerotime():
    return [120, 120, 240]

def strongnote(ornotelist):
    notelist = []
    for i in ornotelist:
        notelist.append(int(i))
    notelist = sorted(notelist)
    for i in notelist:
        if (int(i) + 12) in range(int(notelist[0]), int(notelist[len(notelist)-1]) + 13):
            notelist.append(int(i) + 12)
            notelist = sorted(notelist)
        if (int(i) - 12) in range(int(notelist[0]), int(notelist[len(notelist)-1])): 
            notelist.append(int(i) - 12)
            notelist = sorted(notelist)
    newlist = []
    
    for i in notelist:
        if i not in newlist:
            newlist.append(i)
    return newlist

def bannednote(notelist):
    bannednotelist = []
    for i in strongnote(notelist):
        bannednotelist.append(int(i) + 1)
        bannednotelist.append(int(i) - 1)
    return bannednotelist

