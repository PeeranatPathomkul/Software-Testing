def funnyString(s):
    s_reverse=s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1]))!=abs(ord(s_reverse[i])-ord(s_reverse[i+1])):
            return "Not Funny"
    return "Funny"