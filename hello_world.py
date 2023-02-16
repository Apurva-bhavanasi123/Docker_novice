writes=''
f=open("/app/IF.txt", "r")
first_file=f.read()
f1 = open("/app/Limerick.txt", "r")
second_file=f1.read()
from os import listdir
from os.path import isfile, join
mypath="/app"
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and '.txt' in f[-4:])]
print(onlyfiles)
writes+='files are \n '+'\n'.join(onlyfiles)
l1=len(first_file.split())
l2=len(second_file.split())
print(l1)
writes+="\nlength of first file is "+str(l1)
print(l2)
writes+="\nlength of second is "+str(l2)
print(l1+l2)
writes+="\nlength of total is "+str(l1+l2)

from collections import Counter
count1=dict(Counter(first_file.split()))
items=count1.items()
items=sorted(items,key=lambda x:-x[1])
print(items[:3])
writes+="\n most frequent words are "+'\n'.join([x[0]+" with count "+str(x[1]) for x in items[:3]])
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
#rint("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)
writes+='\n Computer IP is '+IPAddr
f = open("/app/result.txt", "w")
f.write(writes)
f.close()
