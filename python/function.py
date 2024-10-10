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