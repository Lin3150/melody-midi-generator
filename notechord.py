#!/usr/bin/env python
# -*-coding:utf-8 -*-

from pychord import note_to_chord
from pychord import utils, Chord
import random
from notevalue import note2value

def note2chord(chordlist):
    chord = []
    for i in sorted(chordlist):
        temp = utils.val_to_note(int(i) % 12)
        if temp not in chord:
            chord.append(temp)
    n = 0
    while n < 100:
        if note_to_chord(chord): 
            return note_to_chord(chord)[0]
        else:
            random.shuffle(chord)    
            n = n + 1 

def chord2note(chordname):
    a = Chord(chordname)
    notelist = []
    notelist.append(note2value(chordname[0] + str(2)))
    for i in a.components():
        notelist.append(note2value(i + str(4)))
    return sorted(notelist)
        

