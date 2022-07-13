#budget 
T=int(input())
for i in range(T):
    x,y=list(map(int,input().split()))
    Akshat=y*30
    if Akshat<=x:
        print("YES")
    else:
        print("NO")

