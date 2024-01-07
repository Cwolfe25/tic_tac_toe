from Matrix_Stuff import MatrixMonday
r = input("how many rows do you want for your matrix:")
c = input("how many column do you want for your matrix:")
r = int(r)
c = int(c)
trixie = MatrixMonday(r,c)
#trixie = MatrixMonday(3,3)

alice = MatrixMonday(3,3)
for i in range(trixie.rows):
    for j in range(trixie.columns):
        numb = input("what do you want this value to be?")
        
        trixie.set_entry(i,j,numb)


alice.set_entry(0,0,1)
alice.set_entry(0,1,1)
alice.set_entry(0,2,1)
alice.set_entry(1,0,1)
alice.set_entry(1,1,1)
alice.set_entry(1,2,1)
alice.set_entry(2,0,1)
alice.set_entry(2,1,1)
alice.set_entry(2,2,1)
print("Alice Matrix:")
alice.print()
print("Trixie Matrix:")
trixie.print()
mcomb = [trixie,alice]
mp = alice.add(trixie)
print("added matrix")
mp.print()
mpt = alice.times(trixie)
print("multiplied matrix")
mpt.print()
#trixie.scalarTimesRow(4,0)
#trixie.print()
#trixie.switch(0,1)
#trixie.print()
#trixie.comb(2,1,2)
#trixie.print()
inv = trixie.inverse()
inv.print()

# trixie.row_reduce()