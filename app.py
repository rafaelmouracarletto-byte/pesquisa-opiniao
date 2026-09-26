# ENTRADA
excelente = 0
bom = 0
ruim = 0
TOTAL_ENTREVISTADOS = 50

# PROCESSAMENTO
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n Entrevistado {i} ")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Opções de opinião:")
    print("1: EXCELENTE")
    print("2: BOM")
    print("3: RUIM")
    
    opiniao = int(input("Digite o número correspondente à sua opinião: "))
    
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida! Esta resposta não será contabilizada.")

# SAÍDA
print("           RESULTADO DA PESQUISA        ")
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'RUIM': {ruim}")
print(f"c) Quantidade de respostas 'BOM': {bom}")