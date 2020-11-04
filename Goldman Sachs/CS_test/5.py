if __name__ == "__main__":
    banker_num, banker = input().split()
    par_num, par  = input().split()
    ans = set()
    
    # For bankers
    start = 1
    for num in banker.split(','):
        if len(num) == 1:  
            ans.add(f'[{start},{num}]')
            start += 1
        else:
            for x in range(0,len(num),2):
                ans.add(f'[{start},{num[x]}]')
            start += 1
    
    # For participants
    start = 1
    for num in par.split(','):
        if len(num) == 1:
            ans.add(f'[{num},{start}]')
            start += 1
        else:
            for x in range(0,len(num),2):
                ans.add(f'[{num[x]},{start}]')
            start += 1
    # print(ans)

    real_ans = dict()

    for li in ans:
        if int(li[1]) not in real_ans:
            real_ans[int(li[1])] = 1
        else:
            real_ans[int(li[1])] += 1
    
    print(max(real_ans.values()))

