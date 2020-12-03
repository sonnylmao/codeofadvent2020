with open("d3.txt","r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
a = len(content[0])

c = 0
t = 0
for x in content:
    print(x)
    if c > a:
        temp = c
        c = (c % a)
        if temp != c:
            c -+ 1
        if c == 31:
            c = 0
        if x[c] == '#':
            t += 1
    else:
        if c == 31:
            c = 0
        if x[c] == '#':
            t += 1
    c += 3
print(t)
