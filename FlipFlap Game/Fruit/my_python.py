from pathlib import Path

path=Path()
f1=path.glob('*')
for i in f1:
	string='"'+str(i)+'"'
	print(string,end=',')