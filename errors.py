#!/usr/bin/env python3
import os
import sys

# EAFP = Easy to ASK Forgiveness than permission

try:
    
    names = open("names.txt").readlines() # FileNotFoundError
except (FileNotFoundError, ZeroDivisionError) as e:
    print(f"{str(e)}.")
    sys.exit(1)

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)