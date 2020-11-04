def find_max_key(releaseTime,keyPress):
    new_list = [0 for _ in range(len(releaseTime))]
    new_list[0] = releaseTime[0]
    for i in range(1,len(releaseTime)):
        new_list[i] = releaseTime[i] - releaseTime[i-1]
    # releaseTime = releaseTime[::-1]
    long_time = max(new_list)
    idx = []
    for i in range(len(new_list)):
        if new_list[i] == long_time:
            idx.append(i)
    if len(idx) == 1:
        return keyPress[idx[0]]
    else:
        ans = float('-inf')
        for char_idx in range(len(idx)):
            if ord(keyPress[idx[char_idx]]) > ans:
                ans = idx[char_idx]
        return keyPress[ans]


if __name__ == "__main__":
    releaseTime = list(map(int,input().split()))
    keyPress = input().strip()

    key = find_max_key(releaseTime,keyPress)
    print(key)