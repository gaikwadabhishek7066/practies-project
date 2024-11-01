'''
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum
calc_sum(5, 10)

def calc_avg(a, b, c):
    avg = (a + b + c)
    sum = avg/3
    print(sum)
    return sum
calc_avg(2, 4, 6)
'''
'''
cities = ["pune", "mumbai", "nagpur", "ambad", "jalna", "sambhaji nagar"]

def print_len(list):
    for item in list:
        print(item, end = " ")
print_len(cities)
   
cities = ["pune", "mumbai", "nagpur", "ambad", "jalna", "sambhaji nagar"]

def print_len(list):
    print(len(cities))
print_len(cities)
'''
'''
def myfuction(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "orange"]

myfuction(fruits)
'''
'''
def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
calc_fact(7)


def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(2)
'''
'''
#
def odd_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    return num

user = odd_even()
print(user)
#
def my_fun():
    print("hello fun")

my_fun()
#
def my_fun(fname):
    print(fname + " refsnes")

my_fun("Email")
my_fun("Tobies")
my_fun("Linus")

#
def my_fun(*kids):
    print("the youngest child is " +kids[2])

my_fun("Email", "Tobies", "Linus")
#
def my_fun(child3, child2, child1):
    print("the youngest child is " + child3)

my_fun(child1 ="Email", child2 ="Tobies", child3 ="Linus")

#
def my_fun(**kid):
    print("His last name is " + kid["lname"])

my_fun(fname = "Tobies", lname = "refsnes")

#
def my_fun(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]

my_fun(fruits)
#
def my_fun(x):
    return 5 * x

print(my_fun(5))
'''
'''
OOPS
'''
'''
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Myfun(self):
        print("hello my name is " + self.name)
        


p1 = Person("abhi", 22)

p1.Myfun()

#
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(self.fname, self.lname)

class Student(Person):
    pass

x = Student("abhi", "gaikwad")

x.print_name()
'''
'''
#
name = ["Pooja", "Rohit", "Punam", "Abhi",]

def find(name):
    for i in name:
        if i[0] =="P" or i[0] =="p":
            print(i)

find(name)
#
name = ["abhi","karan","bali", "yogesh", "thokal","shubham"]

def disp(name):
    for i in name:
        if len(i) == 4:
            print(i)

disp(name)

#
name = ["abhi", "karan"," bali", "yogesh", "thokal","shubham"]
def previous(L,n):
    c = -1
    for i in L:
        c = c + 1
        if i.lower() == n.lower():
            print("index value is ", c)
            break
        else:
            print("name is not found")
previous(name, "yogesh")

#

L = ["abhi", "bali", 4, 8, "thokal", 9]

c = 0

for i in L:
    if str(i).isdigit():
        L[c] = L[c]*3
        c += 1

print(L)

#

L =[23, 35,44,2.3,41, 33, 11, 55, 63, 77,89,22,44,67]

for i in range(len(L)):
    if L[i]%2 != 0:
        L[i] = L[i]+1
print(L)

#
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is: ",sum/3)

s1 = Student("abhi gaikwad", [89, 76, 90])
s1.get_avg()

#
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, "was credit")
        print("total balance = ",self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 156342)

acc1.debit(1000)

acc1.credit(500)

#
class Cricle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Cricle(21)

print(c1.area())
print(c1.perimeter())

#
class Order:
    def __init__(self, item, price):
        self.item = item 
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price


ord1 = Order("chips", 20)
ord2 = Order("tea", 15)

print(ord1 > ord2)


import re

pattern = "[A-Z]+bhi"

text = ''
my name is bhi i am living from maharastra dist.jalna subdist.ambad
my phone number is 123456789 its Abhi Abhishek Aryan my number oky i am lerning python full stack developer cousre
''
matchs = re.finditer(pattern, text)

for match in matchs:
    print(match)

list1=[10,20,30,40,50]
print()
#Using index
print(list1[0],list1[1],list1[2],list1[3],list1[4])


print()
#Using for loop
for value in list1:
    print(value)

print()
#Using iterator
a=iter(list1)
for value in a:
    print(value)

print()

#Syntax: enumerate(iterable,start=0)

names=["naresh","suresh","ramesh","kishor"]
print(names)
e=enumerate(names,start=1)
for x in e:
    print(x)

print()
print(f'before swapping {list1}')
#method-1
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(f'after swappinh{list1}')

#method-2
list[0],list1[-1],list1[-1],list1[0]
print(f'after sapping {list1}')



print()
list=[23,65,19,90]
pos1=1
pos2=3

print(f'Before swaping{list1}')
list1[pos1-1],list1[pos2-1]=list1[pos2-1],list[pos1-1]
print(f'Ater sawping{list1}')
  #
  # 
  # list1=[10,20,30,40,50]

print()
#Using index
print(list1[0],list1[1],list1[2],list1[3],list1[4])


print()
#Using for loop
for value in list1:
    print(value)

print()
#Using iterator
a=iter(list1)
for value in a:
    print(value)

print()

#Syntax: enumerate(iterable,start=0)

names=["naresh","suresh","ramesh","kishor"]
print(names)
e=enumerate(names,start=1)
for x in e:
    print(x)

print()
print(f'before swapping {list1}')
#method-1
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(f'after swappinh{list1}')

#method-2
list[0],list1[-1],list1[-1],list1[0]
print(f'after sapping {list1}')

'''

print()
list=[23,65,19,90]
pos1=1
pos2=3

print(f'Before swaping{list1}')
list1[pos1-1],list1[pos2-1]=list1[pos2-1],list[pos1-1]
print(f'Ater sawping{list1}')
