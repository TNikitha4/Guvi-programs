#nikitha
import math
ni=int(input())
l=math.log10(ni)/math.log10(2)
if math.ceil(l)==math.floor(l):
	print(0)
else:
	a=(ni-1)//2
	b=a*2
	print(ni-b)
