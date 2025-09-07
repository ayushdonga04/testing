'''n1=int(input("enter no1:"))
n2=int(input("enter no2:"))
n3=int(input("enter no3:"))
if n1>n2 and n1>n3:
    print("n1 is big")
elif n2>n1 and n2>n3:
    print("n2 is big")
else:
    print("n3 is big")
'''
'''
a=eval(input("enter data:"))
if type(a) in (list,tuple,set,str,dict):
    if type(a)==list:
        print("given data is list")
    else:
        print("it is multivalue datatype except list")
else:
    print("no given data is single value data type")    
'''
'''a=input("enter data:")
if len(a)==1:
    if 'A' <= a <='Z' or 'a' <= a <='z':
        if a in 'aeiouAEIOU':
            print('entered char is vowel')
        else:
            print('entered char is consonent')
else:
    print("enter only single char")
'''
'''
unm='ayush'
passwrd='ash@20'
uname=input("enter username:")
password=input("enter password:")
if uname==unm:
    if password==passwrd:
        print(f"login sucessfully to {uname}")
    else:
        print("please enter valid password")
else:
        print("please en4ter valid username")
'''

n1=int(input("enter no1:"))
n2=int(input("enter no2:"))
n3=int(input("enter no3:"))

if n1>n2:
    if n1>n3:
        print("n1 is large")
    else:
        print("n3 is large")
elif n2>n3:
        print("n2 is large")
else:
    print("n3 is large")

