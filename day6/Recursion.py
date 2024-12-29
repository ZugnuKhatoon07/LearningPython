#recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5) #5, 4 =n-1, 3 =n-2, 2 =n-3, 1


#returns n!
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
print(fact(6))
