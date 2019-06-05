"""
ID: kunkun2
LANG: PYTHON3
TASK: test
"""

fin = open ("test.in", "r")
fout = open("test.out","w")
x = fin.read()
G=1
for m in (x.split("\n")):
    print(" ")
    for n in m:
        k=int(ord(n))
        G = k*G
    mod = G%47
    if mod ==27:
        fout.write("GO\n")
    else:
        fout.write("STAY\n")
fin.close()
fout.close()

