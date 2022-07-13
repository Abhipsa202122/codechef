def merge_the_tools(string, k):
    # your code goes here
    c=0
    str=""
    for i in string: 
        if i not in str:
            str+=i
        c+=1
        if c==k:
            print(str)
            c=0
            str=""
            