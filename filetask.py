
import PyPDF2
import re
pdfobj=open("sample.pdf","rb")
pdfReader=PyPDF2.PdfReader(pdfobj)
print(len(pdfReader.pages))

pageObj=pdfReader.pages[0]
pop=pageObj.extract_text()
print(pop)

# def Invoice_number():
#   patterns=re.compile("[0-9]+[0-9]/)H/[0-9]")
#   lol=patterns.findall(pop)
#   print(lol)
def CSTIN():
    patterns=re.compile("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]")
    lol=re.findall(patterns,pop)
    return lol 
def GSTIN():
    patterns=re.compile("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]{1}")
    lol=patterns.findall(pop)
    return lol 
def statecode():
    patterns=re.compile("State Code:.+")
    lol=re.findall(patterns,pop)
    return lol
def state():
    pattern=re.compile("State: \s.+")
    kpop=pattern.findall(pop)
    return kpop
def Invoice_Amount():
    patterns=re.compile("Invoice Amount:.+")
    lol=patterns.findall(pop)
    return lol
pk=Invoice_Amount()
print(pk)
inv="".join(pk)
lu=[]
kpop=[]
Invoice_Amounts=inv.split(":")[0]
Invoice_value=inv.split(":")[1]
lu.append(Invoice_Amounts)
kpop.append(Invoice_value)
dicts={k:v for (k,v) in zip(lu,kpop)}
print(dicts)

s=statecode()
l=state()
pop="".join(l)

State=pop.split(":")[0]
Name=pop.split(":")[1]
lu=[]
pops=[]
lu.append(State)
pops.append(Name)
dicts={k:v for (k,v) in zip(lu,pops)}
print(dicts)

patternu=re.search("State:\s [A-Za-z]\s+",pop)
print(patternu)
print(s)

c=CSTIN()
listeu=['CSTIN']
dictsp={k:v for (k,v) in zip(listeu,c)}
print(dictsp)
k=GSTIN()
listeu=['GSTIN']
dictsp={k:v for (k,v) in zip(listeu,c)}
print(dictsp)



pdfobj.close()
