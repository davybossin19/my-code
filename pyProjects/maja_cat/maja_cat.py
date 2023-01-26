#!/usr/bin/env python3

import os, time

os.system('clear')

cats = ['cat1.txt', 'cat2.txt', 'cat3.txt']
frames = []

for cat in cats:
    with open(cat, 'r', encoding='utf8') as file:
        frames.append(file.readlines())

count = 0
print(frames[0])
os.system('clear')
while count < 35:
    frame = frames[count % 3]
    for i, line in enumerate(frame):
        #Each line of a frame will accumulate 10 spaces with each iteration
        frame[i] = ' '*10 + line
    print("".join(frame))
    count += 1
    time.sleep(0.08)
    os.system('clear')

with open('banner.txt', 'r', encoding = 'utf8') as banner:
    frames.append(banner.readlines())

print("".join(frames[-1]))
time.sleep(2)
os.system('clear')