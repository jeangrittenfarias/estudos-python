# =========================
# Maior Menor ou Igual
# =========================

# numeros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número:"))

# operador
ope = input("Digite a operação (+, -, *, /): ")

if ope == "+":
    print(num1+num2)

elif ope =="-":
    print(num1-num2)

elif ope =="*":
    print(num1*num2)

elif ope == "/" :
    if num2 == 0:
        print("Operação invalida")
    else:
        print(num1/num2)

else:
    print("Operação invalida")