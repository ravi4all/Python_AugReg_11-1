##n = int(input("Enter the number : "))
##
##for i in range(2,n):
##    if n % i == 0:
##        print("Not Prime")
##        break
##else:
##    print("Prime number")


# Prime number in a given interval
min_range = 100
max_range = 200

for i in range(min_range, max_range):

    for j in range(2,i):
        if i % j == 0:
            print("{} is not a prime number".format(i))
            break
    else:
        print("{} is a prime number".format(i))
