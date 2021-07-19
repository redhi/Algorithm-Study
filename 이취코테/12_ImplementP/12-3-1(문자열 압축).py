def solution(s):
    s_len = len(s)
    s_len_arr = [s_len]  # 1~len까지 압축했을때 길이 값

    for i in range(1, s_len):
        compressed = ""
        splited = [s[j:j+i] for j in range(0, s_len, i)] # 개수 단위로 자르기 
        print("sp",splited)
        count = 1

        for k in range(1, len(splited)): # 위에서 자른 배열
            prev, cur = splited[k-1], splited[k]
            if prev == cur:  # 이전 문자와 동일하면
                count += 1
            else:  
                compressed += (str(count) + prev) if count > 1 else prev
                count = 1  # 초기화

        compressed += (str(count) + splited[-1]) if count > 1 else splited[-1]
        s_len_arr.append(len(compressed))

    return min(s_len_arr)  # 최솟값 리턴

print(solution("aabbccab"))
