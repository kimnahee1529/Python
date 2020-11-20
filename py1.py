print(" \"I don't like C language!\"")
print("6^2=", 6**2) #거듭제곱
print("%0.1f" % 3.1415)#3.1
print("%0.3f is the correct answer" % 3.1415)#3.142
a='700'
b=100
a=int(a)
b=str(b)
print(a,type(a))
print(b,type(b))

a=2
b=4
print(a+b,a*b,a/b)
print(3**3,10^2,10/3,30//3)

a=int(input())
b=int(input())
print(a+b)
print(a,"+",b,"=",int(a)+int(b))
print(a,"*",b,"=",int(a)*int(b))
print(a,"/",b,"=","%0.0f" % (int(a)/int(b)))
print(a,"//",b,"=",int(a)//int(b))
print(a,"%",b,"=",int(a)%int(b))

if(a>b):
    print(a)
else:
    print(b)

#a=int(input())
if a<=100 and a>=81:
    print("A")
elif a<=80 and a>=61:
    print("B")
elif a<=60 and a>=0:
    print("C")      

id=input()#000116-2333333->female, -1333333->male
if id[7] =="2":
    print("female")
elif id[7]=="1": 
    print("male")
