import sys
import os
for i in range(0,3):
    for j in range(1,25):
        print('op='+str(i)+' thread='+str(j))
        os.system('echo "task=3,op='+str(i)+',parallel='+str(j)+',access_size=256,stride_size=256" > /proc/lattester')