def isPrince(frogList):
    # 여기에 코드를 작성해 주세요!
    for i in range(len(frogList)):
        d = []
        s=''.join(frogList[i]) # list->str
        d = list(s) # str->list 쪼개서 넣
        print(d)
        if(d[0]=="F"):
            return frogList[i]
    

print(isPrince(['Alice', 'Bob', 'Frog']))
