#!/usr/bin/env python

import sys
import re

fd = sys.argv[1]

text = open(fd).read()
qlist = re.findall("(?:^|%)(.+?)%",text,flags=re.S|re.M)

i = 0

empty = [ 1 for x in xrange(0,1000) ]

quotes = {}
qcmp = {}

for quote in qlist:
  quotes[i] = quote
  qcmp[i] = re.sub("(\s|~|,|\.|'|\"|`|!|-)+"," ",quote.lower())
  qcmp[i] = re.sub(" +"," ",qcmp[i])
  qcmp[i] = dict(zip(qcmp[i].split(),empty)).keys()
  i += 1

del(qlist)

for k,q in qcmp.iteritems(): 
  for k1,q1 in qcmp.iteritems():
    if k == k1:
      continue

    if q == q1:
      print "###################repeat#####################\n"
      print quotes[k1]
      print "##############################################\n"
      continue
     
    if len(q) >= 2*len(q1) or len(q1) > 2*len(q):
      continue

    same = 0
    for i1 in q:
      for i2 in q1:
        if i1 == i2:
          same += 1

    if same >= len(q):
      print "##############################################"
      print quotes[k]+"\n-=-=-=-=-=-=-=-= the same as =-=-=-=-=-=-=-=-\n"+quotes[k1]

