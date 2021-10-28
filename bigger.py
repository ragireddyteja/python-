def function():
    num = 100 - age
    b = num
    print("hi", name, "your 100 years will turn in the year", b + 2021)


name = input("enter your name:")
age = int(input("enter your age:"))

function();

2.


def bigger():
    if (a > b):
        if (a > c):
            largest = a
        else:
            largest = c
    else:
        if b > c:
            largest = b

        else:
            largest = c

        print("big number is: ", largest)


a = int(input())
b = int(input())
c = int(input())
bigger();