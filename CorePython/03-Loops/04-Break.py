##for i in range(0,11):
##    print(i)
##    if i == 6:
##        print("Break the loop")
##        break

for i in range(0,11):
    print(i)

    if i >= 6:
        i += 2
        print("Continue the loop")
        print(i)
        continue
