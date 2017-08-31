n = int(input("Enter the number : "))

temp = n

num = 0

while temp > 0:
    r = temp%10
    num = num + (r**3)
    temp = temp//10

if (num == n):
    print("Armstrong number")

else:
    print("Not Armstrong number")
