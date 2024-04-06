class MatrixMonday:

    def __init__(self, rows, columns):
        self.m1 = [[0 for j in range(columns)] for i in range(rows)]
        self.columns = columns
        self.rows = rows

    def print(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.m1[i][j] == -0:
                    self.m1[i][j] = 0
                print(self.m1[i][j], end="\t")
            print()
            
    def set_entry(self, row, column, value):
        self.m1[row][column] = value

    def get_entry(self, row, column):
        return self.m1[row][column]
    def add(self, other):
        """
        Takes:
        self
        other
        Returns:
        mp
        Variables:
        Self - matrix
        other - matrix
        i - int
        j - int
        temp - int
        mp - matrix
        Self - The first matrix being added
        other - the second matrix being added
        i - the number of rows in the matrix
        j - the number of columns in the matrix
        temp - the temporary place where the sums of the matrixs are kept
        mp - matrix where the sums are stored
        """
        mp = MatrixMonday(self.rows,self.columns)                                       #this creates a new to put the added values into
        if self.rows == other.rows and self.columns == other.columns:                   #makes sure the diamentions are equal
            for i in range(self.rows):                                                  #this takes every row in the matrix
                for j in range(self.columns):                                           #this takes every column in the matrix
                    temp = float(self.m1[i][j]) + float(other.m1[i][j])                 #gets the sum of a data piece in each row and column
                    if int(temp) == temp:                                               #sees if the sum is a whole number
                        temp = int(temp)
                    mp.set_entry(i,j,temp)                                              #sets the sum into the added matrix
        else:
            print("the addition could not go through because the matricies diementiond don't match")
        return(mp)
    def times(self, other):
        """
        Takes: 
        self
        Other
        Returns:
        mp
        Variables:
        self - matrix
        other - matrix
        mp - matrix
        i - int
        j - int
        added - float
        c - int
        r - int
        s1 - float
        o1 - float
        self - matrix bieng multipied
        matrix - matrix multiplying 
        mp - where the products are stored
        i - rows of matrix 1
        j - columns of matrix 2
        added - where the products are added
        c - columns of matrix 1
        r - rows of matrix 2
        s1 - the location of the place in the first matrix
        o1 - the location of the place in the second matrix

        """
        mp = MatrixMonday(self.rows,other.columns)                                      #Creates to matrix to store the products 
        mp.print()                                                 #makes sure the matrixs can be multipied by seeing if rows matrix 1 = colums matrix 2
        for i in range(self.rows):                                                  #goes through the rows of matrix 1    
            for j in range(other.columns):                                          #goes through columns of matrix 2
                   
                added = 0 

                added = float(added)
                for c in range(self.columns):                                       #goes through the columns of matrix 1
                                                     #goes through the rows of matrix 2
                            
                    s1 = self.get_entry(i,c)                                    #finds the values of the locations
                    
                    o1 = other.get_entry(c,j)
                    s1 = float(s1)
                    o1 = float(o1)
                    temp = s1 * o1                                              #multiplies both of the values togeather
                            
                    added = added + temp                                        #adds the product to a temp
                if int(added) == added:                                             #sees if the sum is a whole number
                    added = int(added)        
                mp.set_entry(i,j,added)                                             #sets the sum into the temp matrix

        return(mp)

    def scalarTimesRow(self, numb, row):
        """
        Takes:
        self - matrix
        numb - float 
        row - numb
        Returns:
        self - matrix
        Variables:
        temp - int
        j - int
        times - float
        self - matrix being imported
        numb - the number being multiplied into the row
        row - the row being multipiled into
        temp - where the value and the number are multiplied
        j - the column being multipied 
        times = the value on the matrix
        """
        numb = float(numb)                                                              #converts the imports to the right class
        row = int(row)
        temp = 0
        for j in range(self.columns):                                                   #takes every column of the row (i.e. every value)
            times = self.get_entry(row,j)
            times = float(times)            
            temp = numb * times                                                         #multipies the value by the number
            if int(temp) == temp:                                                       #checks to see if its an whole number
                temp = int(temp)
            self.set_entry(row,j,temp)                                                  #sets the value into the location
        return(self)

    def switch(self, row1, row2):
        """
        Takes:
        self - matrix
        row1 - int
        row 2 - int
        returns:
        self - matrix
        variables:
        j - int
        temp1 - str
        temp2 - str
        self - matrix imported
        j - column being switched
        row1 - first row being switched
        row2 - second row bing switched
        """
        row1==int(row1)                                     #takes 2 rows turns them into integers 
        row2==int(row2)
        for j in range(self.columns):                       #goes through each column and switches row 1 values to row 2 and vice versa
            temp1 = self.get_entry(row2,j)
            temp2 = self.get_entry(row1,j)
            self.set_entry(row1,j,temp1)
            self.set_entry(row2,j,temp2)
        return(self)

    def comb(self,numb,row1,row2):
        """
        Takes:
        self
        numb
        row1
        row2
        Returns: 
        Self
        This function will take a number, multiply it into row1, then add it into row 2
        temp = float
        Inv = float
        temp is just where the added areas are stored
        Inv is to reverse the multiplication on row 1

        """
        self.scalarTimesRow(numb,row1)                                          #multiplies numb into row 1
        temp=0
        for j in range(self.columns):  
            p1 = self.get_entry(row1,j)
            p2 = self.get_entry(row2,j)                                         #takes all the columns of the rows 
            p1 = float(p1)
            p2 = float(p2)               
            temp = p1 + p2
            if temp == int(temp):  
                temp = int(temp)                                                #adds the new row 1 to row 2
            self.set_entry(row2,j,temp)                                         #changes each place of row2 to the sum of row 1 and row 2
        inv = 1 / numb                                                          #takes the inverse of numb and multiplies it into row 1 to reverse the multiplication
        self.scalarTimesRow(inv,row1)
        return(self)
        
    def row_reduce(self):
        """
        takes:
        self
        returns:
        self
        Variables:
        self = matrix
        i = int
        j = int
        temp = float
        inv = float
        numb = float
        self is the matrix being manipulated
        i is the rows 
        j is the columns
        temp is a value being taken
        inv inverses temp
        numb is a value being taken from the matrix
        """
        for i in range(self.rows):                                              #this goes through every row
            for j in range(self.columns):                                       #this goes through all the columns
                if i == j and float(self.get_entry(i,j)) == 1.0:                #sees is checking if the row reduce form is met
                    pass
                elif i < j:                                                     #this skips the ones that are on the other side of the triangle
                    pass
                elif i == j and float(self.get_entry(i,j)) != 1.0:                             
                    temp = float(self.get_entry(i,j))                           #this takes the value
                    if temp != 0:                                               #makes sure the function doesn't break
                        inv = 1 / temp                                          #reverses the row so its this varible becomes 1
                        self.scalarTimesRow(inv,i)
                    else:
                        self.switch[i][i+1]                                     #switches the row if it doesn't works

                elif i > j and int(self.get_entry(i,j)) !=0:                    #if its outside of the upper triangle
                    numb = self.get_entry(i,j)                                  #takes the value so it can be turned to 0
                    numb = float(numb)
                    numb = numb * -1
                    self.comb(numb, j, i)                                       #combines it so its 0
        return(self)


                





    def inverse(self):
        """
        takes:
        self
        returns:
        inverse
        variables:
        self = matrix
        invm = matrix
        r = int
        c = int
        i = int
        j = int
        temp = int
        col = int
        a = int
        b = int
        revert = float
        numb = float 
        ivn = float
        revinv = float
        ic = int
        inverse  = matrix

        self = the matrix being imported in
        invm = the matrix being inverted with the diagonal
        r = the rows of the imported matrix
        c = columns of the second matrix
        i = rows for most for loops
        j = columns for most for loops
        temp = the location for a value when creating the matrix
        col = was used to reach the other side of the big invm matrix
        a = rows
        b = columns
        revert = temp location for a value
        revinv = the inverse of revert
        numb = location of a value in the other row
        ivn = multipied to make it subtraction
        ic = the amount of columns for hte big matrix
        inverse = where the inverse is stored

        """
        if self.rows == self.columns:                                           #makes sure that its a square matrix
            r = int(self.rows)                                                  #gets the rows and columns
            c = int(self.columns)
            check = MatrixMonday(r,c)
            c = c * 2                                                           #creates the new matrix with diagonal matrix
            
            invm = MatrixMonday(r,c)                                            #creates a said matrix
            for i in range(self.rows):                                          #copies the og matrix
                for j in range(self.rows):
                    temp = self.get_entry(i,j)
                    temp = float(temp)
                    invm.set_entry(i,j,temp)

            for i in range(invm.rows):                                          #inputs the diagonal matrix
                col = r+i
                invm.set_entry(i, col, 1)

            invm.row_reduce()                                                   #row reduces this matrix
            for a in range(invm.rows):                                          #goes through the same matrix

                for b in range(self.columns):
                    if a == b and float(invm.get_entry(a,b)) != 1:              #checks to see if the function is in the upper echolon, if not it goes in
                        revert = float(invm.get_entry(a,b))                     #divides the row if its not in diagonal
                        revinv = 1/revert
                        invm.scalarTimesRow(revinv,a)

                    elif a < b and float(invm.get_entry(a,b)) != 0:             #if its on the right side of the diagonal
                        numb = float(invm.get_entry(a,b))                       #takes the number then combines it to cancle it
                        inv = numb * -1
                        invm.comb(inv,b,a)
                        revert = float(invm.get_entry(a,a))                     #reverses what happened to the other row
                        revinv = 1/revert
                        invm.scalarTimesRow(revinv,a)

            r = int(self.rows)                                                  #creates a new matrix to store the inverse
            c = int(self.columns)
            ic = int(invm.columns)
            inverse = MatrixMonday(r,c)

            for a in range(invm.rows):                                          #gets the inverted matrix and imports it into the new one
                for b in range(c,ic):
                    temp = float(invm.get_entry(a,b))
                    if temp == int(temp):
                        temp = int(temp)
                    inverse.set_entry(a,b-c,temp)
            return(inverse)

            


        else:
            print("needs to be a square matrix")

