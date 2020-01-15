#!/usr/bin/python
# five rows labeled each including a-z characters
# with a corresponding column that creates the keycode
# note: total of 26^5 combinations

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