def solution(s):
    S = list(s)
    print(S)
    new = []
    answer = 0
    count = 1
    c_len = 0
    while count>len(S):
        for i in range(len(S)-1):
            if S[i] == S[i+1] or i==0:
                new.append(S[i])
                c_len += 1
                print(i, new)
            else:
                new.append(S[i+1])
                print("else",i,new)
                
        count += 1
    print(count) 
    return answer
solution("aabbaccc")
