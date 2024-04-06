def main():
    from Matrix_Stuff import MatrixMonday
    r = input("how many rows do you want for your first matrix:")
    while r == '':
        r = input("have to enter something here: ")
    c = input("how many column do you want for your first matrix:")
    while c == '':
        c = input("have to enter something here: ")
    r = int(r)
    c = int(c)
    trixie = MatrixMonday(r,c)



    for i in range(trixie.rows):
        for j in range(trixie.columns):
            print("Location:")
            print(i) 
            print(j)
            numb = input("what do you want this value to be for?")
            while numb == '':
                numb = input("have to enter something here: ")
            trixie.set_entry(i,j,numb)
    print("first matrix:")
    trixie.print()

    a = input("how many rows do you want for your second matrix:")
    b = input("how many column do you want for your second matrix:")
    while a == '':
        a = input("have to enter something here: ")
    while b == '':
        b = input("have to enter something here: ")
    a = int(a)
    b = int(b)
    alice = MatrixMonday(a,b)
    for i in range(alice.rows):
        for j in range(alice.columns):
            print("Location:")
            print(i) 
            print(j)
            numb = input("what do you want this value to be for?")
            alice.set_entry(i,j,numb)
        print("second matrix:")
        alice.print()
    destroy = 0
    print("dimentions of 1")
    print(r)
    print(c)
    print("dimentions of 2")
    print(a)
    print(b)
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
            if a == r and b == c:
                mp = alice.add(trixie)
                print("added matrix")
                mp.print()
            print("Matrixies need to be the same shape for addition")
        elif choice == "2":       #need to make another one both ways
            print("you chose matrix multiplication")
            m = input("which matrix do you want to multiply (which matrix do you want to multiply into the other: 1 or 2):? ")
            
            if m == "1" and c == a:
                mpt = trixie.times(alice)
                print("multiplied matrix")
                mpt.print()
            elif m == "2" and r == b:
                mpt = alice.times(trixie)
                print("multiplied matrix")
                mpt.print()
            elif r != b or a != c:
                print("the rows of the first matrix need to match the columns of the second matrix")
            else:
                print("didn't choose a matrix")
        elif choice == "3":
            print("you chose row multiplication")
            row = input("what row do you want to multiply?:")
            while row == '':
                row = input("have to enter something here: ")
            number = input("what number do you want to multiply that row by?: ")
            
            while number == '':
                number = input("have to enter something here: ")
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
            while r1 == '':
                r1 = input("have to enter something here: ")
            r2 = input("what is the second row you want to switch(remember the first row is row 0)?: ")
            
            while r2 == '':
                r2 = input("have to enter something here: ")
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
            while r1 == '':
                r1 = input("have to enter something here: ")
            r2 = input("what row do you want to multiply into to combine with the other row?: ")
            while r2 == '':
                r2 = input("have to enter something here: ")
            numb = input("what number do you want to multiply into the other matrix?: ")
            
            
            while numb == '':
                numb = input("have to enter something here: ")
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
                inv.print()
            elif m == "2" and a == b:
                inv = alice.inverse()
                inv.print()
        elif m == "8":
            destroy = destroy + 1
        else:
            print("you need to choose a function")



if __name__ == "__main__":
    main()