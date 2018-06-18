import os
import time

f = open("list.txt", "r")

for link in f:
    os.system('git clone ' + link)
   
os.system('clear')
print "Thanks for using gitUtilDownloader! Bye!"

time.sleep(3)
os.system('exit')

f.close()
