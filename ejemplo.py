#primera edicion
n = input("ingrese el numero de valores ")
n = int(n)
L = [] #definir lista vacia
#esta estructura va contando desde 0
# hasta n - 1, porque cuenta n elementos
for i in range(n):
    entrada = input ("ingrese el valor ")
    entrada = float(entrada)
    L.append(entrada)

print("los numeros ingreados en formato lista")
print(L)
par = []
for i in range(len(L)):
    if L[i]%2==0:
        print("el numero es par")
        print(L[i])
        par.append(L[i])

print("los valores pares en lista")
print(par)




