#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    totalas = 0
    # Counts almost all a's
    totalas += s.count('a') * int(n/len(s))
    
    # Counts the last iteration if it n is not a complete loop of the len of s
    for i in range(n%len(s)):
        if(s[i] == 'a'):
            totalas += 1
    

    return totalas
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()