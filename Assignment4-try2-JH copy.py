#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:05:24 2019

@author: Jacqui
"""

def frequency_eval(language_file):
    with open(language_file, encoding='utf-8') as f:
        content = f.read()
    Lang = content.split()
    word_count = len(Lang)
    
    List = []
    for word in Lang:
        x = word.lower().strip("*..--!?''")
        List.append(x)
        
    frequency = {}
    for word in List:
        if not word in frequency:
            frequency[word] = 0
        frequency[word] +=1
        
    for word in frequency.keys():
        frequency[word] = frequency[word]/word_count
    sorted_counts = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
    most_frequent = dict(sorted_counts[:10])
    return(most_frequent)
    
print('Spanish Frequency Table: ',frequency_eval('cherbonnel-mi-tio_SP.txt'))
print('German Frequency Table: ',frequency_eval('schloemp-tolle-koffer_DE.txt'))
print('English Frequency Table: ',frequency_eval('eaton-boy-scouts_EN.txt'))
print('Unknown Frequency Table: ',frequency_eval('unknown-lang.txt'))

Spanish_table = (frequency_eval('cherbonnel-mi-tio_SP.txt'))
German_table = (frequency_eval('schloemp-tolle-koffer_DE.txt'))
English_table = (frequency_eval('eaton-boy-scouts_EN.txt'))
Unknown_table = (frequency_eval('unknown-lang.txt'))

Sum_German = 0
Sum_Spanish = 0
Sum_English = 0
for w in Unknown_table.keys():
    German = abs(German_table.get(w,0) - Unknown_table.get(w))
    Sum_German = Sum_German + German
    Spanish = abs(Spanish_table.get(w,0) - Unknown_table.get(w))
    Sum_Spanish = Sum_Spanish + Spanish
    English = abs(English_table.get(w,0) - Unknown_table.get(w))
    Sum_English = Sum_English + English

print("Total word frequency difference between German and Unknown: ",Sum_German)
print("Total word frequency difference between English and Unknown: ",Sum_English)
print("Total word frequency difference between Spanish Unknown: ",Sum_Spanish)

if Sum_Spanish < Sum_English and Sum_Spanish < Sum_German:
    print("I predict Spanish is the language of the Unknown text")

