#!/usr/bin/python
# five rows labeled each with a-z characters
# with a center column that creates key

import string

alphabet = list(string.ascii_lowercase)
combs = []
for i in alphabet:
  for j in alphabet:
    for k in alphabet:
      for l in alphabet:
        for m in alphabet:
          combs.append((i,j,k,l,m))

ct = len(combs)
keys = '\n'.join(''.join(tup) for tup in combs)
newct = '{:,}'.format(ct) 

f = open("keys.txt", "w")
f.write("Possible keys: " + newct + '\n')
f.write(keys)
f.close()