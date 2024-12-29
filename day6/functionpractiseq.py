# ____________****WAP to print the length of a list . (list is the parameter)****______
cities = ["delhi", "gurgaon", "naida", "pue", "siwan", "chenni", "mumbai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]


def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#_______***WAP to print the elements of a list in a single line. (list is the paramenter)***________
cities = ["delhi", "gurgaon", "naida", "pue", "siwan", "chenni", "mumbai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

# print_len(cities)
# print_len(heroes)

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()


#_______***WAP to find the factorial of n. (n is the parameter)****______
def cal_fact(n):
    fact =1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(6)

#____________****WAPto convert USD INR.*****___________
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD", inr_val, "INR")

# converter(10)

def check_number_type(num):
    if num %2 == 0:
        return f"the input number is even."
    else:
        return f"the input numer is odd."
# number = int(input("enter any number :"))

print(check_number_type(4))

