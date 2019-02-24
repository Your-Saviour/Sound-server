import time
textfile = open("sounddatatest.txt", "a+")
#result = time.localtime(time.time())
local_time = time.ctime(time.time())
#while true:
for i in range(1000):
#    result = time.localtime(time.time())
    textfile.write("{}\t{} \r\n".format((i+1), local_time))
#for x in range(10):
#    print("tm_hour:", result.tm_hour)
textfile.close()
