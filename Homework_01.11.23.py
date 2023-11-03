
import math
#1․Write a Python program that calculates the area of a circle based on the radius entered by the user.
radius=int(input("PLease enter the radius of a circle  to calculate its area: "))
area=math.pi*radius**2
print("The circle area is:%0.1f"%(area))

#2․Write a Python program that will print the multiplication table for the given number.
number=int(input("PLease enter the a number  to calculate its multiplication table : "))
for i in range(1,11):
    print(number, "*", i," = ",number*i)

# 3․Write a Python program that will print the sum of a given array’s minimum and maximum elements.
list=[-1,0,-5,10,20]
max_el=list[0]
min_el=list[0]   
sum=0 
for i in list:
    if(i>max_el):
        max_el=i
    if(i<min_el):
        min_el=i
sum=max_el+min_el
print("The sum of array's max and min elements is: ",sum)            

#4.Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
f_name="Adam"
l_name="Smith"
print(f_name, " ",l_name, "reverse order->",f_name[::-1]," ", l_name[::-1])

#5․Write a Python program to count the number 4 in a given list.
list2=[1,4,-5,7,4,8,4,11]
count=0
for i in list2:
    if(i==4):
        count+=1
print("The count of number 4 in the given list is: ",count)

#6․Write a Python program to swap two variables.
x=10
y=20
print("X=",x,"Y=",y)
temp=x
x=y
y=temp
print("Swaped->","X=",x,"Y=",y)

#7.Write a Python program that will reverse the given string./Version 1
string="Hello"
rev_str=string[::-1]
print(string,", reversed string->",rev_str)
                                                           #/Version 2
new_string=""
for i in range(len(string)):
     new_string+=(string[len(string)-i-1])
print(string,", reversed string->",new_string)     

#8․Write a Python program that  solves a quadratic equation of the form ax^2 + bx + c = 0 for real roots.
a,b,c=1,2,1
disc=pow(b,2)-(4*a*c)
if(disc>0):
    x_1=(-b+math.sqrt(disc))/(2*a)
    x_2=(-b-math.sqrt(disc))/(2*a)
    print("The real roots for", a,"x^2 + ",b,"x + ",c, " quadratic equation are: ","X1=","{:.2F}".format(x_1),"X2=","{:.2F}".format(x_2))
elif(disc==0):
    x_1=-b/(2*a)
    print("The real root for", a,"x^2 + ",b,"x + ",c, " quadratic equation is: ",x_1)
else:
    print("The discriminat for",a,"x^2 + ",b,"x + ",c, " quadratic equation is a negative number.")    

#9․Write a Python program to return the sum of all divisors of a number.
num=int(input("Please enter a number to calculate its divisors: "))
div_sum=0
for i in range(2,num):
    if((num%i==0)):
        div_sum+=i
print("The sum of all divisors(1 and the number itself not included)of %0.f is :"%(num),div_sum)        

#10․Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
sequence=input("Please enter a sequence of comma-separated numbers: ")
sep=sequence.split(",")
print("The sequence of numbers as a list: ",sep)
print("The sequence of numbers as a tuple: ",tuple(sep))
