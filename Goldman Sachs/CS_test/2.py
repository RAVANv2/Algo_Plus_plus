def find_max(stock_price):
    ans = 0
    low = high = 0
    i = 0

    while i < len(stock_price) - 1:

        while i < len(stock_price) -1 and stock_price[i] >= stock_price[i + 1]:
            i += 1
        low = stock_price[i]

        while i < len(stock_price) -1 and stock_price[i] <= stock_price[i + 1]:
            i += 1
        high = stock_price[i]

        ans += (high - low)
    return ans
    

if __name__ == "__main__":
    stock_price = list(map(int,input().strip().split()))[1:]
    print(find_max(stock_price))
    