my_list=list(map(int,input().split()))
s_list=[]
arr=my_list.copy()
while arr:
    min_val=arr[0]
    for i in arr:
        if i<min_val:
            min_val=i
    s_list.append(min_val)
    arr.remove(min_val)
print(s_list)
print(s_list[1], s_list[len(s_list)-4])
