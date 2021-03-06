import re

# Functions to check if sequence exists in list

# Naive algorithm

def checkSequence1(arr, seq):
    result = True
    for element in seq:
        try:
            index = arr.index(element) 
            arr = arr[index+1:]
        except ValueError:
            result = False 
            break 

    if result:
        print("Match exists")
    else:
        print("Match doesn't exist")

# Using RegEx
        
def checkSequence2(arr, seq):
    data_str = "".join("<"+str(i)+">" for i in arr)
    attack_str = ".*" + ".+".join("<"+str(i)+">" for i in seq) + ".+"
    x = re.search(data_str, attack_str)
    if x:
        print("Match exists")
    else:
        print("Match doesn't exist")

# Improvised algorithm using two pointers

def checkSequence3(arr, seq):
    i = 0
    j = 0
    while i < len(seq) and j < len(arr):
        if seq[i] == arr[j]:
            i = i + 1
        j = j + 1

    if i==len(seq):
        print("Match exists")
    else:
        print("Match doesn't exist")

# File handling to store contents in list 

with open("winevents_c1.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines] 

# Check if sequence exists in list

seq1 = ["4672", "4663", "4698"]
seq2 = ["4697", "4698", "4658"]

checkSequence3(lines, seq1)
checkSequence3(lines, seq2)
