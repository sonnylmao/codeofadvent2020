with open("Desktop/d3.txt","r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
a = len(content[0])

c = 0
t = 0
#
s1 = 61
s2 = 265
s3 = 82
s4 = 70
s5 = 34
#
odd = 1
for x in content:
    if odd % 2 == 1:
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
        c += 1
    odd += 1
print(t)

print(s1*s2*s3*s4*s5)