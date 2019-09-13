#!/usr/bin/env python
# -*-coding:utf-8 -*-

from melodybar import melodybar
from numpy import random
from random_mode import notetime, strongnote, zerotime, bannednote
from readmidi import analyzechordprogression, analyzemidi

#判断是否重音
def isstrong(time):
     if time % 120 >= 60:
          return False
     else:
          return True

#判断选择音符还是休止符
0
def choosenote(time):
     if isstrong(time):
          random.choice()

def choosezero():
     return 0

def generator(filepath):
     melody = melodybar()
     timestamp = 0
     lastnote = None
     notelist, timelist = analyzechordprogression(filepath)
     breath = 0.8
     
     while not melody.isfull():
          num = 0
          for i in timelist:
               if timestamp > i:
                    num = num + 1
          choice = random.random()
          if choice < breath:
               if lastnote:
                    if isstrong(timestamp):
                         try :
                              ind = 0
                              for i in strongnote(notelist[num]):
                                   if lastnote > i:
                                        ind = ind + 1
                              note = strongnote(notelist[num])[int(ind / 2 * random.randn() + ind / 2)]
                         except:
                              note = -1
                         sustime = random.choice(notetime())
                    else:
                         note = int(10 * random.randn() + lastnote)
                         sustime = random.choice(notetime())    
               else:
                    try:
                         lenn = len(strongnote(notelist[num])) / 2
                         note = strongnote(notelist[num])[int(lenn * random.randn() + lenn)]
                    except:
                         note = -1                         
                    sustime = random.choice(notetime())                                   
          else:
               note = 0
               sustime = random.choice(zerotime())          
 
          if note not in bannednote(notelist[num]):
               if (note in range(int(strongnote(notelist[num])[0]) + 12, int(strongnote(notelist[num])[len(strongnote(notelist[num]))-1]))) | (note == 0):
                    
                    if melody.addmelody(note, sustime):
                         timestamp = timestamp + sustime
                         lastnote = note
                         print('yes, you have added one note')
                    else:
                         print('time is out of scale')
                    
     print(melody.note)               #看要不要添加自动补齐功能
     return melody
               
                    

         
def mutigen(newfile):
     generator('Major Prog 01 (Iadd9-V-vim7-IV).mid').writemelodyfile(newfile)
         
#generator('Major Prog 01 (Iadd9-V-vim7-IV).mid')
mutigen('test01.mid')
                   
               
     
     