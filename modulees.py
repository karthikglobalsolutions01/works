import modules
 
modules.greetings("nani")
k=modules.person1["age"] 
print(k)
p=min(9,8,67)
k=max(90,78,69)
pop=abs(-89.9)
lol=pow(3,4)
import math
x=math.sqrt(64)
math.ceil(1.2)
math.floor(1.9)
#json is there to work with json data
import json
x='{"name":"nani","age":89,"city":"hyderabad"}'
y=json.loads(x)
print(y["age"])
print(x)
print(lol)

print(p)
print(k)
z='{"name":"nani","age":89,"city":"hyderabad"}'
pop=json.dumps(x)#to convert into json

try:
    print(x)
except NameError:
    print("an exception occured")
except:
    print("Something else went wrong")

else:
    print("Nothing went wrong")
finally:
    print("must print statement")
f=open("resume.txt","a")
print(f.read())
print(f.read(5))#to specify the number of characters to accesss
print(f.readline())#will read only 1 line 
f.write("the file is open now and ready to write and i am writing in it ")
print(f.read())
f.close()
import os 
os.remove("resume.txt")


