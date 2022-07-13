T=int(input())
for i in range(T):
    X,Y,A=list(map(int,input().split()))
    if A>=X and A<Y:
       print("yes")
    else:
       print("no")
    # if 1<=T<=10000:
    #     print("yes")
    # elif 20<=X<Y<=40:
    #     print("no")
    # elif 10<=A<=50:
    #     print("yes")
    # else:
    #     print("no")
