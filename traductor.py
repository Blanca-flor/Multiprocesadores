import re


dato=input("ingrese el dato en código ensamblador con el siguiente formato \n nemónico dato1, dato2, dato3 \n ó \n nemónoco dato1, dato2 \n") #se pide el dato con el formato deseado
dato=dato.replace(',','')# se le quitan las comas que no nos sirven
memAd=[int(i) for i in re.findall(r'-?\d+\.?\d*', dato)]# memory Addres se crea una lista int de los números encontrados 
dato=dato.split()#modificamos nuestra lista y la pasamos a un array
dato=dato[0]# de este array solo nos quedamos con el némónico
dicNem={'mov':'0000', 'add':'0001', 'subs':'0010'} # diccionario de Nemónicos, falta agregar demás nemónimos
codM=dicNem.get(dato) #obtenemos en codigo Máquina la equivalencia del nemónico



if (len(memAd)==2): #si es de tamaño dos,a gregamos un cero para que sea de tamaño 3
    memAd.insert(1,0)
#construímos el código mpaquina que falta con base en nuestra lista de numero ya encontrados
if (len(memAd)==3):
    c=0
    while c!=3:
        if len(format(memAd[c], "b"))<4:
            cons=len(format(memAd[c], "b"))
            c2=0
            while c2<4-cons:
                codM=codM + '0'
                c2 =c2+1
            codM=codM + format(memAd[c], "b")
        else:
            codM=codM + format(memAd[c], "b")
        c =c+1

#print (memAd)
#print (dato)
print (codM)
