import json
import os

def load_data(path):
    f = file(path, "r")
    return json.loads(f.read())

def build_data(path):
    d = load_data(path)
    mapping = {}
    meaning = {}
    wordlist = []

    for word in d:
        if not (word[u'word'][0] in mapping):
            wordlist.append(word[u'word'][0])
            meaning[len(mapping)] = []
            mapping[word[u'word'][0]] = len(mapping)
    
    for word in d:
        for m in word[u'meaning']:
            for tmp in m.split():
                if tmp in mapping:
                    meaning[mapping[tmp]].append(mapping[word[u'word'][0]])
    
    
    return mapping, meaning, wordlist
        