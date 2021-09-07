import re
s = "=.="
# #1
ss = s.lower()
# #2
ss = re.sub("[^a-z1234567890._-]","",ss)
# #3
sss,flag = "",True
for i in ss:
    if i == '.':
        if flag:
            sss += i
            flag = False
    else:
        sss += i
        flag = True
# #4
if sss and sss[0] == '.':
    sss = sss[1:]
if sss and sss[-1] == '.':
    sss = sss[:-1]
# #5
if sss == "":
    sss += "a"
# #6
if len(sss) > 15:
    sss = sss[:15]
if sss[-1] == '.':
    sss = sss[:-1]
# #7
while len(sss) <= 2:
    sss += sss[-1]

print(sss)