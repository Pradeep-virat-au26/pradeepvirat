#1
#a=input("entre the number:")
#b=input("entre the numbe:")
#c=input("entre the numbe:")

#if(a>b and b>c) or (c>b and b>a):
    #print(b,"is the biggest")
#elif (b>a and a>c) or (c>a and a>b):
     #print(a,"is the biggest")
#else:
    #print(c,"is the biggest")


#2
#a=input("entre the number:")
#b=input("entre the number:")
#c=input("entre the number:")

#if(a>b and b<c):
   #print(b"second bigger number")
#elif(b>a and a<c):
    #print(a,"second biggest number")
#else:
    #print(c,"bigger number")



#3
a=int(input("entre a number:"))
if (a%3 == 0 and a%5 ==0):
    print("fizzbizz")
elif a%3 ==0:
    print("fizz")
elif a%5 ==0:
    print("bizz")
else:
    print(a)