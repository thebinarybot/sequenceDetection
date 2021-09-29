# Required packages 

import bisect 
from collections import defaultdict

# Function to test if attackSequence exists in dataset

def checkSequence(attackSequence, dataset):

        # Variable to store result
        result = True

        # Edge case : If attack sequence is empty, then result is false
        if len(attackSequence) == 0:
            result = False

        else:
            # Dictionary is used to store dictionary elements in dataset and it's corresponding indices in a list
            indices = defaultdict(list)
            for index, value in list(enumerate(dataset)):
                indices[value].append(index)

            current_sequence = 0

            # Implementing binary search using bisect package for increased efficiency to iterate over huge amount of attack sequences
            for value in attackSequence:
                if value not in indices:
                    result = False
                    break
                current_index = bisect.bisect_left(indices[value], current_sequence)
                if current_index >= len(indices[value]):
                    result = False
                    break
                current_sequence = indices[value][current_index] + 1

        if result:
            print("Match exists")
        else:
            print("Match doesn't exist")

# File handling to store contents in list 

with open("winevents_c1.txt") as file:
    lines = file.readlines()
    lines = list(map(int, [line.rstrip() for line in lines]))

# Check if given sequence(s) exists in list

seq1 = [4672, 4663, 4698]
seq2 = [4697, 4698, 4658]

# Sequence that doesn't exist in array
# seq3 = [4697, 1509839, 4698, 4658]

# Dummy sequence
# seq4 = []

checkSequence(seq1, lines)
checkSequence(seq2, lines)

# checkSequence(seq3, lines)
# checkSequence(seq4, lines)
