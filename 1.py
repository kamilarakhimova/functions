def remove_palindroms(spells): 
    l = spells
    k = 0
    for i in range(len(l)):
        if ' ' in l[k]:
            f = (l[k].lower()).split()
            f = ''.join(f)
        else:
            f = l[k].lower()
        if f == f[::-1]:
            l.pop(k)
            k -= 1
        k += 1
    return l
