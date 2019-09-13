#!/usr/bin/env python
# -*-coding:utf-8 -*-

from pychord import utils
import re

def note2value(note):
    if re.findall(r'\d', note):
        a = utils.note_to_val(re.split(r'\d', note)[0])
        b = re.findall(r'\d', note)[0]

        return (int(b) + 1) * 12 + a
    else:
        return utils.note_to_val(note)

def value2note(value):
    b = value // 12 - 1
    a = value % 12
    name = utils.val_to_note(a)
    number = str(b)
    return name + number

