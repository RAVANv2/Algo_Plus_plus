

t = int(input())

while t:

    t -= 1

    season = int(input())
    time_I = list(map(int, input().strip().split()))
    final_time = 0
    for idx in range(season):
        var = list(map(int,input().strip().split()))
        E = var[0]
        time_E = var[1:]

        if E == 1:
            final_time += time_E[0]
            continue

        dur = time_I[idx]

        final_time += time_E.pop(0)

        for j in range(len(time_E)):
            final_time += time_E[j] - dur

    print(final_time)