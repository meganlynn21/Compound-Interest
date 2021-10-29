# Compound Interest Calculator



#Input

fP = float(input("Enter the starting principal: ") )
fR = float(input("Enter the annual interest rate: ") ) 
iM = int(input("How many times per year is the interest compounded? ") )
iT = int(input("For how many years will the account earn interest? ") )


#Calculate


nFV = fP * ( 1 + ( (fR/100) / iM ) ) ** ( iM * iT)



#Output

print("At the end of", iT , "years. You will have $", format(nFV, ",.2f") )
