def findsword(string, word):
    r=string.find(word)
    if(r==-1):
        return False
    else:
        return True

def findsnumbers(inpt):
    numbers=[]
    r = 0
    currentnumber=''
    for c in inpt:
        if c.isdigit():
            currentnumber+=c
        else:
            if not currentnumber=='':
                numbers.append(int(currentnumber))
                currentnumber=''
    if not currentnumber=='':
                numbers.append(int(currentnumber))
    for x in numbers:
        r+=x
    return r

def main():
    sum=0
    flag=True
    while(True):
        inpt=input()
        inpt=inpt.lower()
        if(findsword(inpt,"on")):
            flag=True
        if(findsword(inpt,"off")):
            sum=0
            flag=False
        if(flag and findsword(inpt,"=")):
            print(f"O Resultado da soma é: {sum}")
        if flag:
            r = findsnumbers(inpt)
            sum+=r

if __name__ == '__main__':
    main()