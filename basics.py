# x,y =input().split()
# print("number of boys ",x)
# print("number of girls",y)
# def nani(a,b):
#     print("addition",a+b)
#     print("substraction",a-b)
#     print("floor division",a//b)
#     print("division",a/b)
#     print("%",a%b)
# k=int(input("enter the first value for arthematic operations"))
# j=int(input("enter the second value for arthematic operations"))
# c=nani(j,k)
# a=5
# print("demo of the command to specify the type of element",type(a))
# b="nani hi nana"
# print(b,type(b))
# print(b[0],"example of the indexing in string")
# l1=["nani","pawan-kalyan",1]
# print(l1[0],"indexing in lists")
# tupe=([1,2,34])
# print("example of tuple",tupe)
# print("example of indexing in tuple ",tupe[0])
# set1={1,2,3,4}
# print("example of set",set1)
# disco={1:"nani",2:"pawan",3:"babu"}
# print("example of dictonary ",disco)
# listu=[1,2,3,4,4,5]
# print("list functions")
# print(listu.append(6),"append function in lists")
# print(listu.pop(),"will remove last element in list pop")
# k='[1,2,3,4]'
# res = k.strip('][').split(', ')



# print(res)
# def even ():
    
#  listses=[1,2,3,4,5,6]
#  l4=[]
# #String methods
# name="karthik konduri"
# print(len(name))
# txt="na peru nani"
# print("nani" in txt)
# txteu="The best thing is staying positive"
# if "best" in txteu:
#     print("yes, best is there")
# txt="the best is me "
# print("me" not in txt)

# b="hello world"
# print("slicing",b[1:3])
# x="hello world"
# print(x.upper(),"upper")
# pop="hello world"
# print(pop.replace("h","p"))
# a="pop,push"
# print(a.split(","),"split method will convert the element into the list based on seperator ")

# a="hello"
# b="finnovo"
# print(a+b,"we will concatenate the strings")
# age=90
# txt="I am this old {}"
# print(txt.format(age),"format will convert it into text it will convert any value into string  and send them into placeholder which is {}")
# #format lopala variable or value we will insert 
# #escape character \
# textus="we are indians\"warriors\"amma memu"
# #escape characters \n \r \t \b 
# pop="amma amma nana  nana "
# print(pop.count("amma"))
# print(pop.find("nana"))
# print(pop.index("nana"))
# print(pop.isalnum(),"is alphnumeric check")
# print(pop.isalpha())
# print(pop.isdigit())
# l=[1,2,3,4,5,6]
# """def even():
#  for i in range(len(l)):
#     if l[i]%2==0:
#         l2=[]
#         l3=[]
#         l3=l2.insert(i,l[i])
#         return l3
# num=even()"""
# #print(list(num))
# lists=[1,2,3,4,5]
# print(lists.remove(4),"it is used to remove the element first occurance")
# print(lists.pop())
# print(lists.sort(),"used to sort in ascending order")
# print(lists.sort(reverse=True),"used to sort in descending order")
# "used to sort according to function consition"
# tuplee=("nani","pawan-kalyan","ntr")
# print(tuplee)
# #to add only 1 element in tuple we need to add , after the first element
# list3=[]
# print(list3.copy())
# del lists[1]
# thistuple=tuple(("apple","banana","cherry"))
# print(thistuple)
# fruits=("apple","banna","cherry","postman")
# nuts=("badam","almond","walnut")
# keka=("popcorn",)
# #methods in tuples AS it is immutable it only has 2 methods and we can either add 2 tuples and multiply the number of elements inside it 
# (green,orange,*yellow)=fruits
# keka+=nuts
# print(keka)
# print(green)
# print(orange)
# print(yellow)
# #sets methods example 
# setu={1,23,34,56,98}
# print(setu)
# setsu={False,"jannu","karthik",0}
# print(setsu)    
# print(len(setsu))
# police=set(("nani","pop","lolipop"))
# print(police)
# thisset={"apple","banana","cherry"}
# for x in thisset:
#     print(x)
# lol={"pop","lol"}
# moye={"moye","moye"}
# lol.update(moye)
# print(lol)
# lol.remove("moye")
# print(lol)
# lol.pop()
# print(lol)#will remove random element
# thisset={"pop","lol","dude"}
# pop={"","avunu ana"}
# for x in thisset:
#     print(x)
# thisset.update(pop)#update=union
# #symmentric_difference_update will remove all common elements and place rest
# #dictonary not allow duplicates
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1990
# }

# print(thisdict["brand"])
# thisdicts={
#     "brand":"porshce",
#     "color":["red","green","purple"]
# }
# lol=dict(name="karthik",age="21",gender="male")
# print(lol)
# print(lol.keys())
# print(lol.values())
# print(lol.items())#willreturn in tuples in a list
# if "name" in lol:
#  print("name in dictonary")
# lol.update({"work":"finnovo"})
# print(lol)
# lol.pop("work")
# print(lol)
# #random element remove
# #the difference between clear and del clear will empty the dictonary but dictonary present del the dictonary completely gone from the memory 
# for x in lol:
#     print(x)
# for x in lol.values():
#     print(x)
# for x,y in lol.items():
#     print(x,y)
# kpop = {
#     "employee1":{
#     "age":"22",
#     "salary":"15k"
#  },

#     "employee":{
#     "age":"23",
#     "salary":"15k"
#  },
# }
# print(kpop)
keys=[1,2,3,4,5]
values=["pani-puri","chori","pooori"]
myDict ={k:v for (k,v) in zip(keys,values)}
# print(myDict)
# #regex used to search the pattern in string 
# import re
# txt="The rain in Spain"
# x=re.search("^The.*Spain$",txt)
# #regex predefined conditions \w matches alphanumeric character
# #\d matches any digits \D non digit \s white-space match \S non white space \W non alpha numeric
# #regx matching plus repeation some time * multiple times the charcater can be matched
# #* will match even if there is no match + atleast 1 match it will match
# #? matches either 1 or zero time {m,n} atleast m repeations max n repeations
# txt="the rain in india"
# x=re.findall("ai",txt)#will return all the repeations of that 

# print(x)
# print(re.search("\s",x))
# print(re.split("\s",txt))
# #print(re.sub("\s","9",txt))
# #there are few methods to retrive data about the search object
# txte="The dancing in the rain"
# x=re.search(r"\bS\w+",txt)
# #print(x.span())#returns start and end positions of the match
# print(x.string)#will return the string 
# print(x.group())#will return only that specific part

# makedict={"name":"nani","age":23}
# for x in makedict:
#     c=x
# print(list(c))
# print(makedict.keys())
list1=[24,26,22,45]
list2=["rupa","madhu","karthik","dilip"]
dicts={k:v for (k,v) in zip(list1,list2)}
print(dicts.get(22))
print(dicts.update({26:"gopal"}))
print(dicts.pop(22))

for x in dicts:
 if x > 30 :
    print(dicts.get(x))
print(dict(age=x,name=dicts.get(x)))
print(dicts.items())
for x in dicts:
    if x == 22:
        print("yes found it ")
import re
x="This is my Pan number ABCTY1234D/ and the pan card numbers as follows BSCPO4563H/ BSDK123456P/ POLPO23456/ AWDFGHHJKK12455"
k=re.split("\s",x)
listsu=[1,2,3,4]
pop=[]
p=str(k).strip('][')
print(p)
y=re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}",x)
for match in y:
  print(match)
  pop.append(match)
print(pop)

dicts={k:v for (k,v) in zip(listsu,pop)}
print(dicts)
# for _ in range(int(input())):
#       name = input()
#       score = float(input())
# lists=[]
# lists.append(name)
# lists.append(score)
# print(lists)

def my_function():
  print("hello from function")
my_function()

def my_functions(fname):
  print(fname+"deepali")
my_functions("nani")
my_functions("my gf")
def my_function(fname,lname):
  print(fname+" "+lname)
my_function("nani","devarakonda")
def royal(*kids):
  print("the charlie kids",kids)
royal("nani","charlie","chaplin")
def royals(child1,child2):
  print("the youngest royals"+child2+child1)
royals(child1="charlie",child2="chaplin")
x= lambda a,b:a*b
print(x(5,6))
y= lambda a,b,c:a+b+c
print(y(1,2,3))
class MyClass:
  x=6
p9=MyClass()
print(p9.x)
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"{self.name}({self.age})"
p1=Person("john",89)
print(p1)

p1=Person("john",90)
print(p1.name)

print(p1.age)
class lol:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def police(lol):
    print("the police name is "+lol.name)
p1=lol("karthik",22)
p1.police()
p2=lol("nani",21)
p2.police()
# del p1
print(p1)
print(p2)
class Teacher:
  def __init__(self,name,position):
    self.name=name
    self.position = position
  def designation(self):
    print("this is lecturers position"+self.position)
  def passtime(self):
    print(self.name+"the pass time is playing chess")
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()
# class office:
#   def __init__(self,fname,lname):
#     self.finame=fname
#     self.laname=lname
#   def registration(self):
#     print("the registration  details"+self.fname,self.lname)
# class details:
#   def __init__(self,fname,lname,payment):
#     super().__init__(fname,lname)
#     self.payment=payment
#   def details(self):
#     print("the name",self.finame+self.laname,"the amount"+self.payment)
# x=details("nani","devarkonda","1000000")
# x.details()
#python itterator
mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
class MyNumbers:
  def __iter__(self):
    self.a=1
    return self
  def __next__(self):
    x=self.a
    self.a +=1
    return x
myclass = MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#polymorphism
class Car:
  def __init__(self,brand,model):
    self.brand = brand
    self.model =model
  def move(self):
    print("Drive")
class Boat:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("sail")
class Auto:
  

 def __init__(self,brand,model):
  self.brand=brand
  self.model=model
 def move(self):
   print("ride")
car1=Car("ford","mustang")
boat1=Boat("ferrari","shipo")
auto1=Auto("mahindra","ace")
for x in (car1, boat1, auto1):
  x.move()
car1.move()#if the same thing happens with the inheritence then child class will over ride the parent  class element
#2 globals closest global value is high that is considered