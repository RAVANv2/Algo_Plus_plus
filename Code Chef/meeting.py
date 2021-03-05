
def convertToHour(time):
    hour_s = int(time[0])*10 + int(time[1])
    hour_e = int(time[9])*10 + int(time[10])

    if time[6] == "P" and hour_s!=12:
        hour_s += 12
        hour_s = str(hour_s)
    elif time[6] == "A" and hour_s == 12:
        hour_s -= 12
        hour_s = "0" + str(hour_s)

    if time[15] == "P" and hour_e!=12:
        hour_e += 12
        hour_e = str(hour_e)
    elif time[15]=="A" and hour_e == 12:
        hour_e -= 12
        hour_e = "0" + str(hour_e)
    return hour_s, hour_e

def convertToMinute(time):
    minute_s = time[3] + time[4]
    minute_e = time[12] + time[13]
    return minute_s, minute_e

def chefTime(time):
    hour = int(time[0])*10 + int(time[1])
    minute = time[3]+time[4]

    if time[6] == "P" and hour!=12:
        hour += 12
        hour = str(hour)
    elif time[6] == "A" and hour == 12:
        hour -= 12
        hour = "0" + str(hour)

    return hour, minute

t = int(input())

while t:
    t -= 1
    chef = input()
    chef_h, chef_m = chefTime(chef)
    friend = int(input())

    for i in range(friend):
        time = input()
        hour_s, hour_e = convertToHour(time)
        minute_s, minute_e = convertToMinute(time)

        print(int(chef_m))
        # if (int(hour_s) <= int(chef_h) and int(hour_e) >= int(chef_h)):
        #     if int(minute_s <= int(chef_m)):
        #         print(1, end='')
        #     else:
        #         print(0, end='')
        # print(0,end='')
    print()

