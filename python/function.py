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

def odd_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
    return num

user = odd_even()
print(user)