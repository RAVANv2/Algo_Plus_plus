
def max_stock(stock_price):
    ans = 0
    new = 0

    for i in range(len(stock_price) - 1):
        for j in range(i+1,len(stock_price)):
            if stock_price[i] < stock_price[j]:
                ans = stock_price[j] - stock_price[i]
                new = max(ans,new)
    return new

if __name__ == "__main__":  
    stock_price = list(map(int, input().strip().split()))[1:]

    print(max_stock(stock_price))
