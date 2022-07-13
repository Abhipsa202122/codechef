#taller
T=int(input("enter"))
i=0
while i<T:
    x,y=map(int,input().split())
    if x>y:
        print("A")
    else:
        print("B") 
    i+=1       