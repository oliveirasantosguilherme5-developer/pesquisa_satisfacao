# Contadores
excelente = 0
bom = 0
ruim = 0
# Respostas
while True:
    resposta = input("Como você avalia nosso serviço? (excelente/bom/ruim) ou digite 'sair' para encerrar: ").lower()
    if resposta == 'sair':
        break
    elif resposta == 'excelente':
        excelente += 1
    elif resposta == 'bom':
        bom += 1
    elif resposta == 'ruim':
        ruim += 1
    else:
        print("Resposta inválida. Por favor, digite 'excelente', 'bom', 'ruim' ou 'sair'.")
# Resultados
print("Resultados da pesquisa de satisfação:")
print(f"Excelente: {excelente}")
print(f"Bom: {bom}")
print(f"Ruim: {ruim}")
