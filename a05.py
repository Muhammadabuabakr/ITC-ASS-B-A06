def word_count(s):
    l_w = ""
    d = {}
    
    for i in s:
        i = i.lower()
        if ord(i)>=48 and ord(i)<=57:
            l_w += i
            
        if ord(i)>=65 and ord(i)<=90:
            l_w += i
            
        if ord(i)>=97 and ord(i)<=122:
            l_w += i
        
        elif ord(str(i))==39:
			l_w += i
            
        
        else:
            l_w += ','

    l_w = l_w.split(',')
    for word in l_w:
        if word == '':
            continue
        if word not in d.keys():
            d[word] = 1
            
        else:
            d[word] += 1
                
    return d

