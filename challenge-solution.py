def solution(s):
    #cg, lg
    cg = 0
    result ={}
    temp = ""
    c = 1
    slen = len(s)
    for i in range(slen):
        if i != slen-1:
            if s[i] == s[i+1]:
                temp += s[i]
                c = 1
            else:
                if c == 1:
                    temp += s[i]
                    c = 0
                else:
                    temp = s[i]
                tlen = len(temp)
                result.update({temp : tlen})
                temp = ""
        
    print(result)
    m = max(result.values())
    print(m)
    num = 0
    for i in result:
        if len(i) < m:
            num += m - len(i)

    print(num)


solution("abaaababbaabba") 