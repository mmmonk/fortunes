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
  quotes[i] = quote # listing normal quotes
  # getting rid of all special characters 
  qcmp[i] = re.sub("(\s|~|,|\.|'|\"|`|!|-|:|;|\)|\()+"," ",quote.lower())
  # making a list of unique words
  qcmp[i] = dict(zip(qcmp[i].split(),empty)).keys()
  # sort them by word length
  qcmp[i].sort(key = lambda x: len(x))
  i += 1

del(qlist)
del(empty)

# sorting the list of words from quotes, by the number of unique words in quote
qcmp = sorted(qcmp.items(),key = lambda x: len(x[1]))
# make copy of the qcmp array
qcmp1 = qcmp[:]

for idx,q in qcmp:
  lq = int(pmatch*len(q)) # number of unique words that we need to match

  try:
    qcmp1.remove((idx,q)) # we don't need to compare to current quote
  except ValueError:
    pass

  # lets print some progress indication
  if len(qcmp1) % 10 == 0 or len(qcmp1) < 200:
    sys.stderr.write("quotes left to check: "+str(len(qcmp1))+"\n")

  for idxq1,q1 in qcmp1:
    same = 0

    # quotes are exactly the same
    if q == q1:
      same = 1

    elif q in q1: # the list of words is part of the other list
      same = 1

    else: # we need to compare word by word
      csame = 0

      for item in q:
        if csame >= lq: # did we already found enough words
          break
        try:
          q1.index(item) # do we have this word in the other quote
          csame += 1
        except ValueError:
          pass

      if csame >= lq:
        same = 1

    if same == 1: # it is probably the same quotes as the other quote ;)
      print "###############################################"
      print quotes[idx]
      print "-=-=-=-=-=-=-=-= the same as =-=-=-=-=-=-=-=-=-"
      print quotes[idxq1]

