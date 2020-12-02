with open("Desktop/coa1.txt","r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]

    ans = []

    count = 1
    for x in content:
        count1 = 1
        for m in range(count,len(content)):
            for n in range(count1, len(content)):
                if int(x) + int(content[m]) + int(content[n]) == 2020:
                    ans.append(int(x)*int(content[m])*int(content[n]))
    print(ans))
