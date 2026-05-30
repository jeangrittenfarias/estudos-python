# =========================
# Verificador de Coleções
# =========================

animais = ["Leão", "Gorila", "Girafa", "Tigre"]

print(animais)

procura = input("Qual animal você procura? ")

if procura in animais:
    print("Animal encontrado")
else:
    print("Animal não encontrado")