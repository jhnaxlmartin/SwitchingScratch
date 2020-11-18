import activeAliasTracker
import json

activeAliasTracker.getactive_index()

with open('C:/Users/john.axl.s.martin/PycharmProjects/SwitchingScratch/switchingScratch/template.json') as templatefile:
    data = json.load(templatefile)

def append_prevIndex():
    data[activeAliasTracker.cleanindex_pattern]["previous_index"] = activeAliasTracker.currentIndex
    return data

append_prevIndex()

