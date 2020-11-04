def check_min_is_coorect(ans_dict,key):
    lower, upper = ans_dict[key]

    for keys,value in ans_dict.items():
        new_lower, new_upper = value
        if key != keys and lower > new_upper:
            return False,new_upper
    return True,0
            
if __name__ == "__main__":
    n,d = list(map(int,input().strip().split()))    
    stock_price = list(map(int,input().strip().split()))
    while d:
        d -= 1
        ans_dict = dict()
        profit = int(input())

        for i in range(len(stock_price)-1):
            for j in range(i,len(stock_price)):
                if stock_price[i] < stock_price[j] and stock_price[j] - stock_price[i] == profit:
                    ans_dict[j-i] = [i+1,j+1]
        # print(ans_dict)
        if ans_dict:
            
            key = min(ans_dict.keys())

            check,upper = check_min_is_coorect(ans_dict,key)

            if not check:
                for keys,value in ans_dict.items():
                    new_lower,new_upper = value
                    if new_upper == upper:
                        if d==0:
                            print(f'{ans_dict[keys][0]} {ans_dict[keys][1]}')
                        else:
                            print(f'{ans_dict[keys][0]} {ans_dict[keys][1]}',end=',')
            else:
                if d==0:
                    print(f'{ans_dict[keys][0]} {ans_dict[keys][1]}')
                else:
                    print(f'{ans_dict[key][0]} {ans_dict[key][1]}',end=',')
        else:
            if d==0:
                print(-1)
            else:
                print(f'-1',end=',')


