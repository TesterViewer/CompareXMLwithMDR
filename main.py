import os
from os.path import basename
import glob
import errno
import re


filespaths = ['..\CompareXMLwithMDR\input\*xml']
mdrpath = '..\CompareXMLwithMDR\input\walk_convert.mdr'
fo = open('..\CompareXMLwithMDR\output\outVCError.txt','w')
fo.write("THIS IS BELOW LIST VC BAD POLL\n")
for filespath in filespaths:
  file = glob.glob(filespath)
  for name in file:
    try:
      with open(name) as f, open(mdrpath) as mdr:
        content = f.readline()
        mdrcontent = mdr.read().splitlines()
        lstXml = []
        isMissing = False
        while content:
          content = f.readline()
          trimStart = "<Source>"
          trimEnd = "</Source>"
          if content.find(trimStart,0,len(content)) != -1:
            resulttemp = content.replace(trimStart, "",1)
            result = resulttemp.replace(trimEnd, "",1)
            result = result.strip();
            result = result +'.'
            lstXml.append(0)
            for index in mdrcontent:
              if index.find(result,0,len(index)) != -1:
                lstXml[len(lstXml) - 1] = 1
        for element in lstXml:
          if element == 0:
            isMissing = True
        if isMissing == True:
          fo.write(f.name+'\n')
      mdr.close()
      f.close()
    except IOError as exc:
      if exc.errno != errno.EISDIR:
        raise
fo.close()
