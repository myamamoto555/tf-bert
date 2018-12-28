#coding:utf-8

pc = 0
nc = 0
with open("output.txt") as f:
    for l in f:
        if "1" in l:
            pc += 1
        if "0" in l:
            nc += 1

print (pc,nc)
