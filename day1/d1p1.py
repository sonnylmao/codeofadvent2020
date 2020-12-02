import numpy as np

with open("coa1.txt","r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]

    ans = []

    count = 1
    for x in content:
        #print(2020-x)
        for m in range(count,len(content)):
            if int(x) + int(content[m]) == 2020:
                ans.append(int(x)*int(content[m]))
    print(ans)
