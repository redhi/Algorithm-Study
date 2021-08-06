def solution(array, commands):
    answer = []
    for i in commands:
        print(array[i[0]-1:i[1]])
        newarr = array[i[0]-1:i[1]]
        newarr.sort()
        print(newarr)
        answer.append(newarr[i[2]-1])
   
    return answer

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4]
print(len(commands))
print(solution(array, commands))

