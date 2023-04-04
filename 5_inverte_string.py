from time import sleep

def inverte_string(string: str):
    """Função recebe string e rearranja as letras em sentido inverso"""
    certinha = list(string)
    invertda = []    
    for letra in certinha:
        invertda.insert(0, letra)
    return ''.join(invertda)




if __name__ == '__main__':
    print('='*30)
    print("INVERTEDOR DE STRINGS TABAJARA".center(30))
    print('='*30)
    entrada = input("Entre com alguma frase/palavra/expressão: ")
    print("\nINVERTENDO...")
    sleep(2) 
    print(f'\n{inverte_string(entrada)}')

