import os
import glob
import errno
import re


filespaths = ['E:\WorkspacePython\CompareXMLwithMDR\input\*xml']
mdrpath = 'E:\WorkspacePython\CompareXMLwithMDR\input\walk_convert.mdr'
for filespath in filespaths:
  file = glob.glob(filespath)
  for name in file:
    try:
      with open(name) as f, open(mdrpath, 'r') as mdr:
        content = f.readline()
        mdrcontent = mdr.read().splitlines()
        countXml = 0
        count = 0
        lstXml = []
        while content:
          content = f.readline()
          trimStart = "<Source>"
          trimEnd = "</Source>"
          if content.find(trimStart,0,len(content)) != -1:
            resulttemp = content.replace(trimStart, "",1)
            result = resulttemp.replace(trimEnd, "",1)
            result = result.strip();
            countXml += 1
            lstXml.append(0)
            for index in mdrcontent:
              if index.find(result,0,len(index)) != -1:
                lstXml[len(lstXml) - 1] = 1
        for element in lstXml:
          if element == 0:
            print "VC wrong"

    except IOError as exc:
      if exc.errno != errno.EISDIR:
        raise
