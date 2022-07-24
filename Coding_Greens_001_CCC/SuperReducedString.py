st = input()
s = []
for c  in st:
    if not s:
        s.append(c)
    elif s[-1] == c:
        s.pop()
    else:
        s.append(c)
if not s:
    print("Empty String")
else:
    print(''.join(s))