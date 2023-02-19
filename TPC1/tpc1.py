import matplotlib.pyplot as plt
import math

def leinfo(ficheiro):
    f=open(ficheiro)
    lista = f.readlines()
    doentes=[]
    #idade,sexo,tensão,colesterol,batimento,temDoença
    min= math.inf
    for pessoa in lista[1:]:
        (idade,sexo,tensao,colesterol,batimento,temdoenca)=pessoa.split(',')
        if temdoenca == "1\n":
            doentes.append((idade, sexo, tensao,colesterol, batimento))
            if(min > int(colesterol)):
                min=int(colesterol)
    return doentes, min


def distporsexo(doentes):
    m=0
    f=0
    for (idade, sexo, tensao, colesterol, batimento) in doentes:
        if (sexo)=="M":
            m+=1
        else:
            f+=1
    return [m,f]

def distporidades(doentes):
    values={}
    for (idade, sexo, tensao, colesterol, batimento) in doentes:
        if f"{(int(int(idade)/5))*5}-{((int(int(idade)/5))*5)+5}" not in values:
            values[f"{(int(int(idade)/5))*5}-{((int(int(idade)/5))*5)+5}"]=1
        else:
            values[f"{(int(int(idade)/5))*5}-{((int(int(idade)/5))*5)+5}"]+=1
    sorted_keys= sorted(values.keys())
    sortedvalues={key:values[key] for key in sorted_keys}
    return sortedvalues

def distporcolestrol(doentes, min):
    values={}
    for (idade, sexo, tensao, colesterol, batimento) in doentes:
        infrange= (int((int(colesterol)-min)/10))*10 + min
        suprange= (int((int(colesterol)-min)/10))*10 + min + 10
        range= f"{infrange}-{suprange}"
        if range not in values:
            values[range]=1
        else:
            values[range]+=1
    sorted_keys= sorted(values.keys())
    sortedvalues={key:values[key] for key in sorted_keys}
    return sortedvalues

def imprimetabela(doentes, scalex =1, scaley=2, fontsize=14):
    data=[]
    data.append(list(doentes.keys()))
    values=[]
    for d in doentes.values():
        values.append(d)
    data.append(values)
    fig, ax = plt.subplots()
    # Hide axes
    ax.axis('off')
    # Create table
    table = ax.table(cellText=data, loc='center')
    # Set font size for table
    table.set_fontsize(fontsize)
    # Set cell height and width
    table.scale(scalex, scaley)
    plt.show()

def main():
    doentes, minc= leinfo("myheart.csv")
    saida=-1
    while saida != 0:
        print("1- Distribuição por sexo")
        print("2- Distribuição por idades")
        print("3- Distribuição por colestrol")
        print("0- Sair")
        saida = int(input("Escolha a distribuiçaõ da doença desejada\n"))
        if saida ==0:
            print("Saindo...")
        elif saida == 1:
            values=distporsexo(doentes)
            print("1-Grafo")
            print("2-Tabela")
            saida = int(input("Escolha Grafo ou Tabela\n"))
            if saida==1:
                fig= plt.figure(figsize = (10, 5))
                plt.bar(["Masculino", "Feminino"], values, color ='maroon', width = 0.2)
                plt.ylabel("Número de doentes")
                plt.title("Distribuição da doença por sexo")
                plt.show()
            else:
                data={}
                data["Masculino"] = values[0]
                data["Feminino"]= values[1]
                imprimetabela(data)
        elif saida == 2:
            values=distporidades(doentes)
            print("1-Grafo")
            print("2-Tabela")
            saida = int(input("Escolha Grafo ou Tabela\n"))
            if saida==1:
                fig= plt.figure(figsize = (10, 5))
                plt.bar(values.keys(), values.values(), width = 0.4)
                plt.ylabel("Número de doentes")
                plt.title("Distribuição da doença por idade")
                plt.show()
            else:
                imprimetabela(values)
        elif saida == 3:
            values=distporcolestrol(doentes,minc)
            print("1-Grafo")
            print("2-Tabela")
            saida = int(input("Escolha Grafo ou Tabela\n"))
            if saida==1:
                fig= plt.figure(figsize = (15, 7))
                plt.bar(values.keys(), values.values(), width = 0.4)
                plt.ylabel("Número de doentes")
                plt.title("Distribuição da doença por colesterol")
                plt.show()
            else:
                imprimetabela(values,4,2 ,fontsize=26)








if __name__ == '__main__':
    main()