import Operaciones as op

num = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

sum = op.sumar(num,num2)
print("Suma: ", sum)

res = op.restar(num,num2)
print("Resta: ", res)

mult = op.multiplicar(num,num2)
print("Multiplicacion: ", mult)

div = op.dividir(num,num2)
print("Division: ", div)