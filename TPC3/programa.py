import json
import math
import re
import collections

from matplotlib import pyplot as plt

def insertnomes(seculosnomes, anostring, nomes):
    ano = int(anostring)
    if ano % 100 == 0:
        seculo = ano//100
    else:
        seculo = ano//100 + 1
    if seculo not in seculosnomes:
        seculosnomes[seculo]=[]

    seculosnomes[seculo].append((nomes[0], nomes[1]))

def leinfo(ficheiro):
    f=open(ficheiro)
    lista = f.readlines()
    data = {}
    seculosnomes={}
    relacoes= {}
    numProcessos=0
    for pro in lista:
        if pro[0].isdigit():
            numProcessos+=1
            ano= re.search(r"\d+::(\d+).*?::", pro).group(1)
            nomes = re.search(r"::([a-zA-Z]+).*?([a-zA-Z]+)::", pro).groups()
            rel = re.findall(r",(\w[A-Za-z ]*\w)\.", pro)
            for relas in rel:
                rela=relas.lower()
                if rela not in relacoes:
                    relacoes[rela]=1
                else:
                    relacoes[rela]+=1
            insertnomes(seculosnomes, ano, nomes)
            if ano not in data:
                data[ano]=1
            else:
                data[ano]+=1  
    print(relacoes)
    return data, seculosnomes, relacoes, numProcessos

def processosPorAno(data, numProcessos):
    fig= plt.figure(figsize = (10, 5))
    plt.bar(data.keys(), data.values(), color ='maroon', width = 0.2)
    plt.ylabel("Quantidade de anos")
    plt.title("Frequencia de processos por data")
    plt.show()

def top5Nomes(seculosnomes, seculo):
    print(seculosnomes[seculo].__class__)
    nomes = seculosnomes[seculo]
    dicproprio = {}
    dicapelido = {}
    for proprio, apelido in nomes:
        if proprio not in dicproprio:
            dicproprio[proprio]=1
        else:
            dicproprio[proprio]+=1
        if apelido not in dicapelido:
            dicapelido[apelido]=1
        else:
            dicapelido[apelido]+=1
    sortedproprio = collections.OrderedDict(dicproprio, reverse=True)
    sortedapelido = collections.OrderedDict(dicapelido, reverse=True)

    print(f"TOP 5 NOMES no Século {seculo}")
    print("NOMES PROPRIOS: ")
    for proprio in list(sortedproprio.keys())[:5]:
        print(f"{proprio}")
    print("----------------------")
    print("APELIDOS: ")
    for apelido in list(sortedapelido.keys())[:5]:
        print(f"{apelido}")


def frequenciarel(relacoes, rels):
    rel=rels.lower()
    if rel not in relacoes:
        print(f"Há 0 {rel}")
    else:
        print(f"Há {relacoes[rel]} {rel}")

def convertjson(ficheiro):
    jsonfile =''
    f=open(ficheiro)
    lista = f.readlines()
    file = open("processos.json", "w")
    for line in lista[:20]:   
        match = re.search("(?P<Pasta>\d+)::(?P<Data>\d+-\d+-\d+)::(?P<Nome>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)::(?P<Pai>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)?::(?P<Mae>[A-Za-z]+[A-Za-z ]*?[A-Za-z]+)?::(?P<Outro>.*?)::",line).groupdict()
        json.dump(match,file)
        file.write(",\n")
        
def main():
    data, seculosnomes, relacoes, numProcessos = leinfo("processos.txt")
    saida=-1
    while saida != 0:
        print("1- Frequencia de processos por ano")
        print("2- Frequencia de nomes proprios e apelidos top 5")
        print("3- Frequencia de relações")
        print("4- Converter 20 registos em Json")
        print("0- Sair")
        saida = int(input("Escolha a cena que quer\n"))
        if saida ==0:
            print("Saindo...")
        elif saida == 1:
            processosPorAno(data, numProcessos)
        elif saida == 2:
            seculo= int(input("Que século deseja? \n"))
            top5Nomes(seculosnomes, seculo)
        elif saida == 3:
            rel = input("Que relação deseja saber a frequencia?")
            frequenciarel(relacoes,rel)
        elif saida ==4:
            convertjson("processos.txt")

if __name__ == '__main__':
    main()