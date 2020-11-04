from collections import Counter
def occ(arr,i,out,key,occ_cnt):

    if i==len(arr):
        return

    if arr[i]==key:
        occ_cnt['cnt']+=1
        out.append(i)
    
    occ(arr,i+1,out,key,occ_cnt)



if __name__ == "__main__":
    arr = [1,2,3,4,5,3,3,2,3,3,22,4]
    out = []
    key = 3
    occ_cnt = {'cnt':0}
    occ(arr,0,out,key,occ_cnt)
    print(out,occ_cnt)


