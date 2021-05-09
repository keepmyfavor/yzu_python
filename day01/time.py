import time

seconds = time.time()

local_time = time.ctime(seconds)

print(local_time)

print(time.ctime())

print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))