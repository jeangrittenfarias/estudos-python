# =========================
# Verificador de idade
# =========================

idade = int(input("Qual é a sua idade? "))

if idade >= 0 and idade <= 17:
    print(f"tendo {idade} você é menor de idade")
    print(f"Faltam {18-idade} anos para  você se tornar adulto")
elif idade >= 18 and idade <= 59:
    print(f"tendo {idade} você é maior de idade")
    print(f"Você já é adulto a {idade-18} anos")
elif idade >= 60 and idade <=130:
    print(f"tendo {idade} você é idoso")
    print(f"Você é idoso a {idade-60} anos e adulto a {idade-18} anos")
else:
    print("Você não tem essa idade kkkk")


    
