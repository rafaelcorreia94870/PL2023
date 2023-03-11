import re
import json

regular1= r"\b(\w+)({[\d,]+}(::\w+)?)?\b"
ex="ex5"
file = open(ex+".csv")

lines = file.readlines()
groupsraw= re.findall(regular1,lines[0])
groups={}
objetos = []
groups['chaves']=[]
print(groupsraw)
for keys,quantidade,op in groupsraw:
    if keys not in groups:
        groups[keys]=[]
    if (quantidade):
        groups[keys].append(quantidade)
    else:
        groups[keys].append(1)
    if(op):
        groups[keys].append(op)
    groups['chaves'].append(keys)

print(groups)

for line in lines[1:]:
    reading=re.split(",|\n",line)
    new={}
    N =len(groups.keys())
    i=0

    for key in groups["chaves"]:
        q=groups[key]
        print(q)
        print(q[0])
        if q[0]!=1:
            print("mais que um")
            if(re.match(r"{(\d),(\d)}",q[0])):
                print("dois valores")
                maxes=re.match(r"{(\d),(\d)}",q[0]).groups(2)
                print(maxes)
                max=int(maxes[1])
                print(max)
            else:
                print("1 valor")
                max=re.match(r"{(\d)}",q[0])
                print(max)
        else:
            max=0
        if(len(q)>1):
            print("len>1")
            sum=0

            if re.search('media',q[1]):
                sum=0
                k=0
                for j in range(0,max):
                    if(reading[i+j]!=''):
                        print(reading[i+j])
                        sum+=int(reading[i+j])
                        k+=1
                new[key]=sum/k
            else:
                sum=0
                for j in range(0,max):
                    if(reading[i+j]!=''):
                        print(reading[i+j])
                        strx=reading[i+j]
                        x=int(strx)
                        sum=sum+x
                new[key]=sum
        else:
            if(reading[i]!=''):
                new[key]=reading[i]
        i+=max+1
    objetos.append(new)

filefinal= open(ex+".json", "w")
json.dump(objetos,filefinal,indent=0,ensure_ascii=False)
print(objetos)
        