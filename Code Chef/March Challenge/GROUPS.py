


t = int(input())

while t:

    t -= 1

    s = input().strip()

    group = 0

    for i in range(len(s)-1):
        if s[i] ==  s[i+1] and s[i] == '1' and s[i+1] == '1':
            continue
        elif s[i] != s[i+1] and s[i]=='1':
            group += 1

    if s[-1] == '1':
        group += 1

    print(group)