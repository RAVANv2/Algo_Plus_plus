def canFormPalindrome(s):
    bitvector = 0
    for str in s:
        bitvector ^= 1 << ord(str)
    return bitvector == 0 or bitvector & (bitvector - 1) == 0


str = "acbbbadzdz"

print(canFormPalindrome(str))