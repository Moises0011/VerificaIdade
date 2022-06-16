nome = str(input("Qual é o seu nome: "))
ano_nas = int(input("Em que ano você nasceu? "))
ano_atual = int(input("Em que ano nós estamos? "))
idade = (ano_atual - ano_nas)
if idade >= 18:
    print("Oi!", nome, "você atingiu a maior idade com", idade, "anos")
else:
    print("Oi!", nome, "você é menor de idade com", idade, "anos")
