#!/usr/bin/env python
# -*-coding:utf-8 -*-

class chord:
    def __init__(self):
        self.time = None
        self.chordnote = []
    
    def addnote(self, note):      
        self.chordnote.append(note)
    
    def addtime(self, time):
        self.time = time
        
class chordbar:
    def __init__(self):
        self.bar = []
    def addchord(self, chord):
        self.bar.append(chord)
        