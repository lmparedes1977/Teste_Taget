
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'OUTROS': 19849.53
}


if __name__ == "__main__":
    
    print('='*40)
    print('RELAÇÃO DE FATURAMENTO / ESTADO'.center(40))
    print('='*40)
    print(f'{"ESTADO":<}{"R$":>15}{"%":>18}\n')
    for chave,valor in faturamento_estados.items():
        percent = valor / sum(faturamento_estados.values())
        centro = 25 - len(chave)
        direita = 23 - len(str(valor))
        print(f'{chave:<}{valor:>{centro}}{percent*100:>{direita}.2f}')
    
