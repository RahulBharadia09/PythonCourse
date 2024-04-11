# Rule 1 : str and numeric values can operate together with *

a,b = 2,3
txt = "@"
print(2*txt*3) #@@@@@@

# Rule 2 : str and str can be operate with + (Concatenation)
A,B = "2",3
text = "#"
print((A+text)*B) # 2#2#2# Precendence rule

# Rule 3 :Numeric value can operate with all arithmetic operators 
C = 10
print(a+B*C) #32 Precendence rule

#Rule 4 : Arithmetic expression with int and float will result in float
D = 12.3
print(a*D)

# Rule 5 : Result of division operator with two integer will be float
print(B/C)

# Rule 6 : integer division with float and int will give int display as float
print(C//B)
