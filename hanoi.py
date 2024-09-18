# Input the number of layers for this hanoi tower, 
# demonstrate the transporting process 
# 输入河内塔的层数, 展示出搬运过程.
def Hanoi(X, Y, Z, n):
	global A, B, C
	if n==1:
		print(f"--> from tower({X}) move 1 piece to tower({Z})")	
		if X=='A':
			temp=A.pop(0)
		elif X=='B':
			temp=B.pop(0)
		else:
			temp=C.pop(0)
		if Z=='A':
			A.insert(0, temp)
		elif Z=='B':
			B.insert(0, temp)
		else:
			C.insert(0, temp)
		print_towers()
		return	
	Hanoi(X, Z, Y, n-1)
	Hanoi(X, Y, Z, 1)
	Hanoi(Y, X, Z, n-1)

def print_towers():
	X=A.copy()
	Y=B.copy()
	Z=C.copy()
	while len(X)<n_layer:
		X.insert(0,'')
	while len(Y)<n_layer:
		Y.insert(0,'')
	while len(Z)<n_layer:
		Z.insert(0,'')
	max_width=n_layer*2+1
	print(f"{'(A)':{max_width}}|{'(B)':{max_width}}|{'(C)':{max_width}}") 
	for x,y,z in zip(X,Y,Z):
		print(f'{x:^{max_width}}|{y:^{max_width}}|{z:^{max_width}}')
	print() 
	
def build_tower(n_layer):
	for i in range(n_layer):
		A.append('*'*(2*i+1))

A=[]
B=[]
C=[]
n_layer=int(input("Hanoi Tower, how many layers (>=1): "))
build_tower(n_layer)
print_towers()
Hanoi('A', 'B', 'C', n_layer)
