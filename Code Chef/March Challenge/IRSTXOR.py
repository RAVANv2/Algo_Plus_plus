

t = int(input())

while t:
    t -= 1
    num = int(input())

    bit_num = bin(num)[2:]

    one = []
    two = []

    one.append('1')
    two.append('0')

    for i in bit_num[1:]:
        if i == '1':
            one.append('0')
            two.append('1')
        else:
            one.append('1')
            two.append('1')

    print(int(''.join(one), 2)*int(''.join(two),2))




