import os
import glob
import errno
import re

filespaths = ['C:\Users\TIEN_CERT\Desktop\Temp\Workspace\input\*xml','C:\Users\TIEN_CERT\Desktop\Temp\Workspace\input\*mdr']
for filespath in filespaths:
  file = glob.glob(filespath)
  for name in file:
    try:
      with open(name) as f:
        content = f.readline()
        count = 0
        while content:
          content = f.readline()
          trimStart = "<Source>"
          trimEnd = "</Source>"
          if content.find(trimStart,0,len(content)) != -1:
            resulttemp = content.replace(trimStart, "",1)
            result = resulttemp.replace(trimEnd, "",1)
            count += 1
            print result + "There are: "+ str(count)
    except IOError as exc:
      if exc.errno != errno.EISDIR:
        raise
