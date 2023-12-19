listey=[1,2,3,4]
l3=[]
setu={}
p=0
for i in range(len(listey)):
    if(listey[i]%2==0):
     l3.insert(i,listey[i])   
print(l3)
lol="nani {} in and as {}"
quality="natural-star"
cinema="nana"
print(lol.format(quality,cinema))
l1=[1,2,3,4]
l2=[2,3,4,5]
pop=set(l1)
pops=set(l2)
pop.difference_update(pops)
print(list(pop))
pp=[1,2,3,4,5]
ll=[4,5,6,7,8]
oo=[]
po=[]
for i in pp:
    if(i not in ll):
        po.append(i)
        
print(po)
print(ll)
oo=[x for x in pp if x not in ll]
# po=[x for x in ll if x not in pp]

print(oo)
# print(po)
