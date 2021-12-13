import re
import sys
input = sys.stdin.readline

HTML = re.split('<main>|<div title|<',input())
tmp = ''
for item in HTML:
    if item:
        if item[0] == '=':
            print('title :',item[2:-2])
        elif item == '/p>':
            tmp = ' '.join(tmp.strip().split())
            print(tmp)
            tmp = ''
        else:
            for i in range(len(item)):
                if item[i] == '>':
                    tmp += item[i+1:]
                    break