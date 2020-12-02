with open("d2.txt","r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]

tc = 0
for x in content:
    a = [char for char in x]
    s = ''
    for x in a:
        if x.isalpha() == True:
            s = x
            break
    pos = 0
    for x in a:
        if x == '-':
            break
        else:
            pos += 1
    s1 = ''
    imp1 = s1.join(a[0:pos])
    
    pos1 = 0
    for x in a:
        if x == ' ':
            break
        else:
            pos1 += 1
    s2 = ''
    imp2 = s2.join(a[pos+1:pos1])
    b = a[pos1+4::]

    ccc = 0
    if b[int(imp1)-1] == s:
        ccc += 1
    if b[int(imp2)-1] == s:
        ccc += 1
    if ccc == 1:
        tc += 1
print(tc)
