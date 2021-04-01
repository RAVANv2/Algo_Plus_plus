


t = int(input())

while t:
    t -= 1
    s = input()
    s1 = s.replace("10","")
    if s1 == ''.join(sorted(s1)):
        print("YES")
    else:
        print("NO")