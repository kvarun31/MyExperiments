GTH = 9
THRSLD = 32
CURR = 2011

def apl_amount(time, amt = THRSLD):
    if time == 0:
	return amt
    amt = int((100*amt*1.0)/(100+GTH))
    return apl_amount(time-1, amt)

amt_dict = {}
map(lambda x: amt_dict.update({x:apl_amount(x)}),[x for x in xrange(50) if apl_amount(x)>0])

for x in range(max(amt_dict.keys())+1):
  print 'Year %s : INR %s' %((CURR-x), amt_dict[x]) 
