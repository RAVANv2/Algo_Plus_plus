t = int(input())


while t:
    t -= 1

    n = int(input())

    array = list(map(str, input().strip().split()))

    goodName = list(list())
    for name in array:
        goodName.append([name[0],name[1:]])

    ans = 0
    for i in goodName:
        for j in goodName:
            z = 0
            if i[0] != j[0]:

                x = j[1]

                for char in x:
                    if i[1].find(char) == 1:

                        z += 1

                ans += (len(i[1]) - z)*(len(j[1]) - z)


    print(ans)