t=int(input("enter"))
i=0
while i<t:
    N,M,O,P=map(int,input().split())
    print(max(N,M,O,P))
    i+=1
