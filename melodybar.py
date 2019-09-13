#!/usr/bin/env python
# -*-coding:utf-8 -*-

from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo


class melodybar:
    def  __init__(self):
        self.note = []
        self.timestamp = []
        
    def addmelody(self, note, time):    
        if time + sum(self.timestamp) <= 7680:
            self.note.append(note)
            self.timestamp.append(time)
            return True
        else:
            return False
            
    def isfull(self):
        if sum(self.timestamp) == 7680:
            return True
        else:
            return False
        
    def writemelodyfile(self, filepath, bpm = 120):
        mid = MidiFile()
        
        track = MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage('set_tempo', tempo = bpm2tempo(bpm)))
        for num in range(len(self.note)):
            track.append(Message('note_on', note=self.note[num], velocity=100, time=0))
            track.append(Message('note_off', note=self.note[num], velocity=100, time=self.timestamp[num] * bpm / 120))
        mid.save(filepath)
    