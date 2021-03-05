

t = int(input())

while t:

    t -= 1
    D,C = list(map(int,input().strip().split()))
    day1 = list(map(int,input().strip().split()))
    day2 = list(map(int,input().strip().split()))

    # Calculate with Charges
    amt = 0
    for i in day1:
        amt += i
    amt += 2*D
    for i in day2:
        amt += i

    # With coupon
    amtCop1 = 0
    for i in day1:
        amtCop1 += i

    amtCop2 = 0
    for i in day2:
        amtCop2 += i


    amtCop = amtCop2 + amtCop1

    if amtCop1 >= 150 and amtCop2 >= 150:
        amtCop += C
    elif (amtCop1 < 150 and amtCop2 >= 150) or (amtCop1 >= 150 and amtCop2 < 150) :
        amtCop += D
        amtCop += C
    elif amtCop1 < 150 and amtCop2 < 150:
        amtCop += 2*D


    if amtCop - amt < 0:
        print("YES")
    else:
        print("NO")




