def solution(answers):
    answer = []
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5] 
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    
    count=[0]*3
    
    
    for i in range(len(answers)):
        if arr1[i%5] == answers[i]:
            count[0] +=1
        if arr2[i%8] == answers[i]:
            count[1] +=1
        if arr3[i%10] == answers[i]:
            count[2] +=1
    
    maxcount = max(count)

    for i in range(3):
        if count[i]==maxcount:
            answer.append(i+1)

    print(answer)
    return answer

answer = [1,2,3,4,5]
solution(answer)
answer2 = [1,3,2,4,2]
solution(answer2)

