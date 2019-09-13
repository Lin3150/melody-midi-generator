#!/usr/bin/env python
# -*-coding:utf-8 -*-

from mido import Message, MidiFile, MidiTrack
import re
from chord import chord, chordbar
from notechord import note2chord

def analyzemidi(file):
    mid = MidiFile(file)
    for i, track in enumerate(mid.tracks):
        temp = 'note_off'
        num = 1
        chbar = chordbar()    
        for msg in track:
            msg = str(msg)  
            if 'note_on' in msg:
                if temp == 'note_on':
                    a = re.findall(r'note=\d\d', msg)[0].split('=')[1]
                    exec('chord%s.addnote(a)'%num)
                else:
                    exec('chord%s = chord()'%num)
                    a = re.findall(r'note=\d\d', msg)[0].split('=')[1]
                    exec('chord%s.addnote(a)'%num)
                    temp = 'note_on'
            elif 'note_off' in msg:
                if temp == 'note_off':
                    pass
                else:
                    time = re.findall(r'time=\d+', msg)[0].split('=')[1]
                    exec('chord%s.addtime(time)'%num)
                    exec('chbar.addchord(chord%s)'%num)
                    num = num + 1
                    temp = 'note_off'
            else:
                pass
        dic = {}
        for chord in chbar.bar:
            dic[str(note2chord(chord.chordnote))] = chord.time
        return dic

def analyzechordprogression(file):
    mid = MidiFile(file)
    for i, track in enumerate(mid.tracks):
        temp = 'note_off'
        num = 1
        chbar = chordbar()    
        for msg in track:
            msg = str(msg)  
            if 'note_on' in msg:
                if temp == 'note_on':
                    a = re.findall(r'note=\d\d', msg)[0].split('=')[1]
                    exec('chord%s.addnote(a)'%num)
                else:
                    exec('chord%s = chord()'%num)
                    a = re.findall(r'note=\d\d', msg)[0].split('=')[1]
                    exec('chord%s.addnote(a)'%num)
                    temp = 'note_on'
            elif 'note_off' in msg:
                if temp == 'note_off':
                    pass
                else:
                    time = re.findall(r'time=\d+', msg)[0].split('=')[1]
                    exec('chord%s.addtime(time)'%num)
                    exec('chbar.addchord(chord%s)'%num)
                    num = num + 1
                    temp = 'note_off'
            else:
                pass
        chordlist = []
        time = []
        timestamp = 0
        for chord in chbar.bar:
            timestamp = timestamp + int(chord.time)
            chordlist.append(chord.chordnote)
            time.append(timestamp)
        return chordlist, time  
    


