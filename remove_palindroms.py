def remove_palindroms(spells): 
     k = 0
     for i in range(len(spells)):
         if ' ' in spells[k]:
             f = (spells[k].lower()).split()
             f = ''.join(f)
         else:
             f = spells[k].lower()
         if f == f[::-1]:
             spells.pop(k)
             k -= 1
         k += 1
     return spells
