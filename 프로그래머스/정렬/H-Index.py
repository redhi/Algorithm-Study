def solution(citations):
    citations = sorted(citations)
    h_list = []
    
    m = min(citations)
    if min(citations) >= len(citations):
        m = len(citations)
        
    for i in range(m,max(citations)+1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
        if count >= i:
            h_list.append(i)
        
    if h_list:
        return h_list[-1]
        
    return 0
