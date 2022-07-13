#Rating improvement:
T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    if y>=x and y<=x+200:
        print("YES")
    else:
        print("NO")
    
