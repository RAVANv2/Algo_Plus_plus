def find_angram(in_str,dict_patern,pattern):
    substring = len(pattern)

    while substring <= len(in_str):
        dict_str = {}
        string = in_str[substring - len(pattern):substring]
        for char in string:
            if char not in dict_str:
                dict_str[char] = 1
            else:
                dict_str[char] += 1
        if dict_patern == dict_str:
            print(substring - len(pattern),end=' ') 
        substring += 1
    
if __name__ == "__main__":
    pattern = "ABCD"
    in_str = "BACDGABCDA"
    dict_patern = {}

    for char in pattern:
        if char not in dict_patern:
            dict_patern[char] = 1
        else:
            dict_patern[char] += 1
    
    find_angram(in_str,dict_patern,pattern)
