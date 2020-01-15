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

keys = '\n'.join(''.join(tup) for tup in combs)
ct = '{:,}'.format(len(combs))

f = open("keys.txt", "w")
# .write("Possible keys: " + ct + '\n')
f.write(keys)
f.close()