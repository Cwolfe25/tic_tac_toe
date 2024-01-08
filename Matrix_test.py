from Matrix_Stuff import MatrixMonday
r = input("how many rows do you want for your first matrix:")
c = input("how many column do you want for your first matrix:")
r = int(r)
c = int(c)
trixie = MatrixMonday(r,c)
#trixie = MatrixMonday(3,3)


for i in range(trixie.rows):
    for j in range(trixie.columns):
        print("Location:")
        print(i) 
        print(j)
        numb = input("what do you want this value to be for?")
        trixie.set_entry(i,j,numb)
print("first matrix:")
trixie.print()

a = input("how many rows do you want for your second matrix:")
b = input("how many column do you want for your second matrix:")
a = int(r)
b = int(c)
alice = MatrixMonday(a,b)
for i in range(trixie.rows):
    for j in range(trixie.columns):
        print("Location:")
        print(i) 
        print(j)
        numb = input("what do you want this value to be for?")
        alice.set_entry(i,j,numb)
    print("second matrix:")
    alice.print()
destroy = 0
while destroy == 0:
    print("functions:")
    print("matrix addition = 1")
    print("matrix multiplication = 2")
    print("row multiplicaiton = 3")
    print("row switch = 4")
    print("linear combination = 5")
    print("row reduction = 6")
    print("find inverse = 7")
    print("quit the proram = 8")
    choice = input("what function do you want to preform:")
    if choice == "1":
        print("you chose matrix addition")
        mp = alice.add(trixie)
        print("added matrix")
        mp.print()
    elif choice == "2":       #need to make another one both ways
        print("you chose matrix multiplication")
        m = input("which matrix do you want to multiply (which matrix do you want to multiply into the other: 1 or 2):? ")
        if m == "1":
            mpt = trixie.times(alice)
            print("multiplied matrix")
            mpt.print()
        elif m == "2":
            mpt = alice.times(trixie)
            print("multiplied matrix")
            mpt.print()
        else:
            print("didn't choose a matrix")
    elif choice == "3":
        print("you chose row multiplication")
        row = input("what row do you want to multiply?:")
        number = input("what number do you want to multiply that row by?: ")
        row = int(row)
        number = float(number)
        m = input("which matrix do you want to do this to?(1 or 2)?: ")
        if m == "1":
            trixie.scalarTimesRow(number,row)
            trixie.print()
        elif m == "2":
            alice.scalarTimesRow(number,row)
            alice.print()
        else:
            print("you didn't choose a matrix")
    elif choice == "4":
        print("you chose row switch")
        r1 = input("what is the first row you want to switch(remember the first row is row 0)?: ")
        r2 = input("what is the second row you want to switch(remember the first row is row 0)?: ")
        r1 = int(r1)
        r2 = int(r2)
        m = input("which matrix do you want to do row swich (1 or 2)?: ")
        if m == "1" and r1 <= r and r2 <= r and r1 >= 0 and r2 >= 0 :
            trixie.switch(r1,r2)
            trixie.print()
        elif m == "2" and r1 <= a and r2 <= a and r1 >= 0 and r2 >= 0 :
            alice.switch(r1,r2)
            alice.print()
        elif r1 > r or r1 < 0:
            print("your first row was outside domain")
        elif r2 > r or r2 < 0:
            print("your second row was outside domain")
        elif r1 > a or r1 < 0:
            print("your first row was outside domain")
        elif r2 > a or r2 < 0:
            print("your second row was outside domain")
        else:
            print("you didn't choose a matrix")
    elif choice == "5":
        print("you chose linear combination")
        r1 = print("what is the row you want to be combined into?: ")
        r2 = input("what row do you want to multiply into to combine with the other row?: ")
        numb = input("what number do you want to multiply into the other matrix?: ")
        numb = float(numb)
        r1 = int(r1)
        r2 = int(r2)
        m = input("what matrix do you want to combine into(1 or 2)?: ")
        if m == "1" and r1 <= r and r2 <= r and r1 >= 0 and r2 >= 0:
            trixie.comb(numb,r2,r1)
            trixie.print()
        elif m == "1" and r1 <= a and r2 <= a and r1 >= 0 and r2 >= 0:
            alice.comb(numb,r2,r1)
            alice.print()
        elif r1 > r or r1 < 0:
            print("your first row was outside domain")
        elif r2 > r or r2 < 0:
            print("your second row was outside domain")
        elif r1 > a or r1 < 0:
            print("your first row was outside domain")
        elif r2 > b or r2 < 0:
            print("your second row was outside domain")
        else:
            print("you didn't choose a matrix")
    elif choice == "6":
        print("you chose row reduce")
        m = input("which matrix do you want to row reduce(1 or 2)?: ")
        if m == "1":
            trixie.row_reduce()
            trixie.print()
        elif m == "2":
            alice.row_reduce()
            alice.print()
        else:
            print("you didn't choose a matrix")
    elif choice == "7":
        print("you chose inverse")
        m = input("what matrix do you want to invert(1 or 2)?: ")
        if m =="1" and r == c:
            inv = trixie.inverse()
            print(inv)
        elif m == "2" and a == b:
            inv = alice.inverse()
            print(inv)
    elif m == "8":
        destroy = 1
    else:
        print("you need to choose a function")



