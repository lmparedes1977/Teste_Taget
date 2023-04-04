import json



if __name__ == "__main__":
    with open('dados.json', 'r', encoding='utf-8') as arq:
        dados = json.load(arq)

    faturamento_mes = dias_uteis = faturamento_medio =0
    for i in range(len(dados)):
        if dados[i]["valor"] > 0:
            faturamento_mes += dados[i]['valor']
            dias_uteis += 1

    faturamento_medio = faturamento_mes / dias_uteis
    maior_faturamento = dias_acima_media = dia_menor_faturamento = dia_maior_faturamento = 0
    menor_faturamento = dados[0]['valor']
    for i in range(len(dados)):
        if dados[i]['valor'] > 0 and dados[i]['valor'] > maior_faturamento:
            maior_faturamento = dados[i]['valor']
            dia_maior_faturamento = dados[i]['dia']
        if dados[i]['valor'] > 0 and dados[i]['valor'] < menor_faturamento:
            menor_faturamento = dados[i]['valor']
            dia_menor_faturamento = dados[i]['dia']
        if dados[i]['valor'] > faturamento_medio :    
            dias_acima_media += 1
    
    print(f'\nConsiderando as informações contidas no arquivo "dados.json", temos que:\n' +
          f'\nO {dia_menor_faturamento}º foi o dia de menor faturamento com R$ {menor_faturamento:.2f};\n' +
          f'O {dia_maior_faturamento}º foi o dia de maior faturamento com R$ {maior_faturamento:.2f};\n' +
          f'Em {dias_acima_media} dias do mês o faturamento foi superior ao faturamento médio mensal (R$ {(faturamento_medio):.2f}, considerando os dias úteis).'
          )
