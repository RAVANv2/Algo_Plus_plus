import math
if __name__ == "__main__":
    str_in = input()
    string_len = 0
    real_str = ''
    k = 0
    for text in str_in.split():
        string_len += len(text)
        real_str += text

    row = math.floor(string_len**0.5)
    col = math.ceil(string_len**0.5)

    if row*col < string_len:
        row = row + 1
    
    output = [['0' for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if k > len(real_str)-1:
                continue
            else:
                output[i][j] = real_str[k]
                k += 1

    ans = []

    for i in range(col):
        out = ''
        for j in range(row):
            if output[j][i] != '0': 
                out += output[j][i]      
            else:
                continue
        ans.append(out)

    for text in ans:
        print(text,end=' ')