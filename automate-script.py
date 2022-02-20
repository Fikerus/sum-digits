#!/usr/bin/env python3

from subprocess import run
from sys import argv

argv.pop(0)

if len(argv)<1 or len(argv)>2:
    print("Error:")
    print("    This program takes one or two positional arguments")
    print("")

def main(argv):
    x=1
    y=1
    if len(argv)==1:
        y=int(argv[0])
    if len(argv)==2:
        y=int(argv[1])
    for i in range(x,y+1):
        run(["./sum-digits.py",f"{i}"])

main(argv)
