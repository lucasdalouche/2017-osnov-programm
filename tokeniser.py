import sys

x=sys.stdin.readlines()

f=1

for s in x:
	s =  s.strip() 
	if s== "" :
		continue
	print("# sent_id = ",f)
	print("# text =",s)
	f=f+1
	s=s.replace(","," ,").replace("."," .")
	t=s.split(" ")
	z=1
	for r in t:
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_'% (z,r))
#		print(z,"\t",r,"\t","_","\t","_","\t","_","\t","_","\t","_")
		z=z+1
	print()