I=input()

D=dict()

S=""

t=1

for i in I:
    if i not in S:
        S+=i
        D[i]=1
    else:
        D[i]=D[i]+1
print(D)
