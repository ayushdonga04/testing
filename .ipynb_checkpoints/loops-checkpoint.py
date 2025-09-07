'''
i=0
while i<10:
    print("python")
    i+=1
'''
'''
i=1
while i<101:
    print(i)
    i+=1
'''
'''
i=200
while i<=300:
    if i%2==0:
        print(i,end=" ")
    i+=1
'''
'''
s1=input("enter string:")
os=""
i=0
while i<len(s1):
    if 'A' <= s1[i] <= 'Z':
        os=os+s1[i]
    i+=1
print(os)
'''
'''
s1=input("enter string:")
us=""
ls=""
ds=""
sss=""

i=0
while i<len(s1):
    if 'A' <= s1[i] <= 'Z':
        us+=s1[i]
    elif 'a' <= s1[i] <= 'z':
        ls+=s1[i]
    elif '0' <= s1[i] <= '9':
        ds+=s1[i]
    else:
        sss+=s1[i]
    i+=1
print(us)
print(ls)
print(ds)
print(sss)
'''

'''
l1=[1,2,34,6,4]
first_value=l1[0]
tp=True
i=0
while i<len(l1):
    if type(l1[i])!=type(first_value):
        tp=False
        break
    i+=1
print(tp)
if tp:
    print("homogenious")
else:
    print("heterogenious")
'''
'''
a=input("enter string:")
j=0
for i in a:
    if j%2!=0:
        print(i)
    j+=1

print("second way \n")

for i in range(1,len(a),2):
    print(a[i])
'''

'''
a=input("enter string:") 
up=0
lo=0
dg=0
ss=0
upl=[]
lwl=[]
dgl=[]
ssl=[]
for i in a:
    if 'A' <= i <= 'Z':
        upl.append(i)
        up+=1
    elif 'a' <= i <= 'z': 
        lwl.append(i)
        lo+=1    
    elif '0' <= i <= '9':
        dgl.append(i)
        dg+=1
    else:
        ssl.append(i)
        ss+=1

print(f"uppercase char {upl} count:{up}")
print(f"lowercase char {lwl} count:{lo}")
print(f"uppercase {dgl} count:{dg}")
print(f"special char {ssl} count:{ss}")
'''
'''
for i in range (350,500):
    if i%5==0 and i%10==0:
        print(i,end=" ")
'''
'''
a=input("enter string:")
rs=''
for i in a:
    rs=i+rs

if a==rs:
    print("plaindrom")
else:
    print("not palindrom")
'''
'''
no=input("enter no:")
rno=''
for  i in no:
    rno=i+rno

print(int(rno))
'''
'''
#prime number
no=int(input("enter no:"))
con=0
for i in range(2,no):
    if no%i==0:
        con=con+1

if con==0:
    print("no is prime")
else:
    print("no is not prime")
'''
'''
#armstrong number
no=int(input("enter no:"))
nos=str(no)
p=len(nos)
print(p)
ans=0

for i in nos:
    dg=int(i)
    ans+=dg**p
   
if no==ans:
    print("number is armstrong")
else:
    print("number is not armstrong")


no=int(input("enter no:"))
p=len(str(no))
ans=0
'''
'''
no=int(input("enter no:"))
i=no
ans=0
p=len(str(no))
while i>0:
    d=i%10
    ans+=d**p
    i=i//10
  
  

print(ans)

if no==ans:
    print("number is armstrong")
else:
    print("number is not armstrong")
'''
