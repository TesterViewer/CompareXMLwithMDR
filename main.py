import os
from os.path import basename
import glob
import errno
import re

filespaths = ['..\CompareXMLwithMDR\input\*xml']
mdrpath = '..\CompareXMLwithMDR\input\input_mdr.mdr'
fo_error = open('..\CompareXMLwithMDR\output\outVCError.txt','w')
fo = open('..\CompareXMLwithMDR\output\outVC.txt','w')
fo_error.write("THIS IS BELOW LIST VCs DO NOT IN MDR\n")
fo.write("THIS IS BELOW LIST VCs IN MDR\n")
strFKey = '<IsKey>false</IsKey>'
strKey = '<IsKey>true</IsKey>'

for filespath in filespaths:
  file = glob.glob(filespath)
  for name in file:
    try:
      with open(name) as f, open(mdrpath) as mdr:
        content = f.readline()
        mdrcontent = mdr.read().splitlines()
        lstXml = []
        isMissing = False
        isKey = True
        while content:
          content = f.readline()
          trimStart = "<Source>"
          trimEnd = "</Source>"
          if content.find(strFKey,0,len(content)) != -1:
            isKey = False
          if content.find(strKey,0,len(content)) != -1:
            isKey = True
          if isKey == True:
            if content.find(trimStart,0,len(content)) != -1:
              resulttemp = content.replace(trimStart, "",1)
              result = resulttemp.replace(trimEnd, "",1)
              result = result.strip();
              if result.find(".0",len(result) -2,len(result)) == -1:
                result = result +'.'
              lstXml.append(0)
              for index in mdrcontent:
                if index.find(result,0,len(index)) != -1:
                  lstXml[len(lstXml) - 1] = 1
        if lstXml == []:
          isMissing = True
        for element in lstXml:
          if element == 0:
            isMissing = True
        if isMissing == True:
          fo_error.write(f.name+'\n')
        else:
          fo.write(f.name+'\n')
      mdr.close()
      f.close()
    except IOError as exc:
      if exc.errno != errno.EISDIR:
        raise
fo_error.close()
fo.close()



