def solution(s):
    answer = 0
    str_list = []
    is_break = False

    if len(s) == 1:
        str_list.append(s)

    for i in range(1, len(s)):
        new_str = ""
        idx = 0
        for j in range(0, len(s), i):
            if is_break:
                is_break = False
                break

            now_str = s[j : j + i]
            count = 1
            # 반복 횟수
            repe = (len(s) - j - 1) // i
            repe_count = 0
            if repe == 0:
                new_str += now_str
                
            if idx <= j:
                for k in range(j + i, len(s), i):
                    compare_str = s[k : k + i]
                    repe_count += 1
                    
                    if now_str == compare_str:
                        count += 1
                    else:
                        if count > 1:
                            idx = k
                            new_str += str(count) + now_str
                        else:
                            new_str += now_str
                        break
                    if repe_count == repe:
                        if count > 1:
                            new_str += str(count) + now_str
                        else:
                            new_str += now_str
                        is_break = True
                        break
        str_list.append(new_str)
    str_list.sort(key=lambda x: len(x))
    answer = len(str_list[0])
    return answer


s = "ababcdcdababcdcd"
s = "aabbaccc"
s = "abcabcdede"
s = "abrabcabcadqabcabc"
s = "abcabcabcdabcfabcabcabczabcabcdddabc"
s = "acdhdh"
s = "xztjabcdabcd"
s = "fabababab"
s = "aaaaaaaaaabbbbbbbbbb"
s = "aaaaa"
s = "aaaaaaaaaa"
s = "aaaaaaaaaabb"
s = "aaaaaaaaaa"
# s = "aaaabbaa"
print(solution(s))
