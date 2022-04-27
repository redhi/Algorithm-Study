from collections import defaultdict


def solution(word, pages):
    word = word.lower()
    answer = 0
    page_list = defaultdict(list)
    for idx, page in enumerate(pages):
        page3 = []
        for i in range(len(page)):
            if page[i].isalpha():
                page3.append(page[i].lower())
            else:
                page3.append(" ")
        page3 = "".join(page3)
        while page3.count("  ") > 0:
            page3 = page3.replace("  ", " ")

        page3 = page3.split(" ")
        word_count = 0
        for i in range(len(page3)):
            if word == page3[i]:
                word_count += 1

        meta_str = '<meta property="og:url" content="https://'

        url_idx = page.index(meta_str)
        basic_url = page[url_idx + len(meta_str) :].split('"/>')[0]
        body = page.split("<body>\n")[1:][0]
        r_body = body.split('<a href="https://')
        out_list = []
        for i in range(1, len(r_body)):
            outside_link = r_body[i].split('">')[0]
            out_list.append(outside_link)

        page_list[basic_url].extend([out_list, word_count, len(out_list), idx])

    key_list = list(page_list.keys())
    answer_list = defaultdict(int)

    for i in range(len(list(key_list))):
        rel_list, word_count, rel_count, idx = page_list[key_list[i]]
        answer_list[key_list[i]] += word_count
        if rel_count == 0:
            give_score = 0
        else:
            give_score = word_count / rel_count
        for j in range(len(rel_list)):
            if page_list.get(rel_list[j]):
                answer_list[rel_list[j]] += give_score

    for i in range(len(list(key_list))):
        if page_list.get(key_list[i]):
            page_list[key_list[i]].append(answer_list[key_list[i]])

    page_list = sorted(page_list.items(), key=lambda x: (-x[1][4], x[1][3]))

    answer = page_list[0][1][3]

    return answer


word = "blind"
pages = [
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://a.com"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href="https://b.com"> Link to b </a>\n</body>\n</html>',
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://b.com"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href="https://a.com"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href="https://c.com"> Link to c </a>\n</body>\n</html>',
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://c.com"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href="https://a.com"> Link to a </a>\n</body>\n</html>',
]
word = "Muzi"
pages = [
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://careers.kakao.com/interview/list"/>\n</head>  \n<body>\n<a href="https://programmers.co.kr/learn/courses/4673"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>',
    '<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n  <meta charset="utf-8">\n  <meta property="og:url" content="https://www.kakaocorp.com"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2\n\n\t^\n</body>\n</html>',
]

print(solution(word, pages))
