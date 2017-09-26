import sys

x=sys.stdin.readlines()

e=1

for s in x:
	print(e,"\t",s)
	e=e+1
	s=s.replace(","," ,").replace("."," .")
	t=s.split(" ")
	z=1
	for r in t:
		print(z,"\t",r,"\t","_","\t","_","\t","_","\t","_","\t","_")
		z=z+1