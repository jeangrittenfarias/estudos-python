# =========================
# Tela de Login
# =========================

login = "Jean"
senha = "123"

tentativa_login = input("Digite seu login")
tentativa_senha = input("Digite sua senha")

if tentativa_login == login and tentativa_senha == senha:
    print("Acesso Liberado!")
else:
    print("Acesso negado!")