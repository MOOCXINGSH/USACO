"""
ID: kunkun2
LANG: PYTHON3
TASK: ride
"""

fin = open ("ride.in", "r")
fout = open("ride.out","w")
x= fin.readlines()
G =1
w =1
for n in x[0]:
    print(x[0])
    if 'A'<=n and 'Z'>=n:
        print(n)
        k=int(ord(n))-64
        print(k)
        G = G*k
        print(G)
for i in x[1]:
    print(x[1])
    if 'A'<=i and 'Z'>=i:
        print(i)    
        j=int(ord(i))-64
        print(j)
        w=j*w
        print(w)
mod1=G%47
mod2=w%47
print(mod1)
if mod1==mod2:
    fout.write("GO\n")
else:
    fout.write("STAY\n")


