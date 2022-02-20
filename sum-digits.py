#!/usr/bin/env python3

from sys import argv

STR_PRINT=False

def usage():
    print("usage:")
    print("    shikovFunction <number>")
    print("")
    print("output:")
    print("    All numbers concatenated from 1 to N")
    print("    Sum of all digits in the number above")

argv.pop(0)

if len(argv)>2:
    print("Error:")
    print("    This program takes one or two positional arguments")
    print("")
    usage()
    exit(1)

if argv[0]=="--help":
    usage()
    exit(0)

if "--string" in argv:
    argv.pop(argv.index("--string"))
    STR_PRINT=True

if int(argv[0])<1:
    print("Error:")
    print("    Argument cannot be less than one")
    print("")
    usage()
    exit(1)

def fun(n,str_print):
    s=""
    for i in range(1,n+1):
        s+=str(i)
    if str_print:
        print(s)
    sum=0
    for i in s:
        sum+=int(i)
    print(sum)

fun(int(argv[0]),STR_PRINT)
