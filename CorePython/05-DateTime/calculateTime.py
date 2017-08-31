import time

start = time.time()

for i in range(100000000):
    pass

end = time.time()
res = end - start
print("Total time : ",res)
