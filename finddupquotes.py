#!/usr/bin/env python

import sys
import re

fd = sys.argv[1]

pmatch = 1
try:
  pmatch = float(sys.argv[2])
except:
  pass

text = open(fd).read()
qlist = re.findall("(?:^|%\n)(.+?)\n%\n",text,flags=re.S|re.M)

empty = [ 1 for x in xrange(0,100) ]

quotes = {}
qcmp = {}

i = 0
for quote in qlist:
  quotes[i] = quote
  qcmp[i] = re.sub("(\s|~|,|\.|'|\"|`|!|-|:|;|\)|\()+"," ",quote.lower())
  qcmp[i] = dict(zip(qcmp[i].split(),empty)).keys()
  qcmp[i].sort(key = lambda x: len(x))
  i += 1

del(qlist)
del(empty)

qcmp = sorted(qcmp.items(),key = lambda x: len(x[1]))
qcmp1 = qcmp[:]

for idx,q in qcmp:
  lq = int(pmatch*len(q))

  try:
    qcmp1.remove((idx,q))
  except ValueError:
    pass

  if len(qcmp1) % 10 == 0 or len(qcmp1) < 200:
    sys.stderr.write("quotes left to check: "+str(len(qcmp1))+"\n")

  for idxq1,q1 in qcmp1:
    same = 0

    if q == q1:
      same = 1

    elif q in q1:
      same = 1

    else:
      csame = 0

      for item in q:
        if csame >= lq:
          break
        try:
          q1.index(item)
          csame += 1
        except ValueError:
          pass

      if csame >= lq:
        same = 1

    if same == 1:
      print "###############################################"
      print quotes[idx]
      print "-=-=-=-=-=-=-=-= the same as =-=-=-=-=-=-=-=-=-"
      print quotes[idxq1]

