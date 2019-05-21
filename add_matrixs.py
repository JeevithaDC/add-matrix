def read():
	m=[]
	i=0
	while i<r:
		l=[]
		j=0
		while j<c:
			x=int(raw_input())
			l.append(x)
			j=j+1
		m.append(l)
		i=i+1
	return m
def display(m):
	for row in m:
		for x in row:
			print x,
		print
def add(a,b,r,c):
	m=[]
	i=0
	while i<r:
		l=[]
		j=0
		while j<c:
			x=a[i][j]+b[i][j]
			l.append(x)
			j=j+1
		m.append(l)
		i=i+1
	return m
	
r = int(raw_input("enter the number of row:"))
c = int(raw_input("enter the number of column:"))
print "enter data"
m1=read()
display(m1)
r = int(raw_input("enter the number of row:"))
c = int(raw_input("enter the number of column:"))
print "enter data"
m2=read()
display(m2)

p=add(m1,m2,r,c)
display(p)
