# Entrada de dados
aparelho=input("Qual é o aparelho que será utilizado? ")
potencia_aparelho=float(input("Qual é a potência do aparelho (Watts)? "))
tempo_medio=float(input("Qual o tempo médio de uso diário (Horas)? "))

# Regiões e suas tarifas (em R$/kWh)
tarifas_regiao={
    "Norte":0.975,
    "Nordeste":0.925,
    "Centro-Oeste":0.875,
    "Sudeste":0.825,
    "Sul":0.75
}

# Loop para garantir uma região válida
while True:
    regiao=input("Qual é a região? ").strip().capitalize()
    tarifa=tarifas_regiao.get(regiao)

    if tarifa is not None:
        break
    else:
        print("Região inválida. Por favor, digite uma das opções: Norte, Nordeste, Centro-Oeste, Sudeste ou Sul.\n")

# Processamento de dados
consumo_mensal=(potencia_aparelho*tempo_medio*30)/1000
custo_estimado=consumo_mensal*tarifa

if tarifa is not None:
    custo_estimado=consumo_mensal*tarifa
else:
    print("Região não reconhecida.")
    custo_estimado=None

# Saída
print(f"\nConsumo estimado do(a) {aparelho} é de {consumo_mensal:.2f} kWh por mês.")
print(f"Tarifa média aplicada: R$ {tarifa:.2f} por kWh")
print(f"Custo estimado mensal: R$ {custo_estimado:.2f}")
