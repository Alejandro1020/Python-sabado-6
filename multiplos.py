# 1.Construir un programa que permita ingresar N (cantidad digitada por
# el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
# fueron ingresados (+1)

multiplos2=0
multiplos3=0

cantidad=int(input('Ingrese la cantidad de numeros '))



for multiplos in range(cantidad):
    numero=int(input('Digite numero '))
    if numero %2==0:
        multiplos2=multiplos2+1
    if numero %3==0:
        multiplos3+=1

print(f'los multiplos de 2 son {multiplos2}')
print(f'los multiplos de 3 son {multiplos3}')
        
     