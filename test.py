def median(li):
  num_len = len(li)
  if num_len % 2 != 0:
    sor_li = sorted(li)
    if num_len <= 1:
      return sor_li[num_len - 1]
    else:
      idx = num_len / 2
      return sor_li[idx]
  else:
    print "fucks"
    sor_li = sorted(li)
    print sor_li
    idx = num_len / 2
    res = sor_li[idx - 1] + sor_li[idx]
    res = res / 2.0
    return res

print median([4,5,5,4])
    