
def tratamento(n):
    """Função de tratamento de entrada de dados pelo usuário"""
    while True:
        try:
            n = int(n)
            break
        except ValueError:
            n = input("Entrada inválida. Por gentileza, entre com um NÚMERO inteiro positivo: ")
    return n

def fibonacci(n):
    """Calulo de sequencia de fibonacci, recebendo inteiro positivo e retornando print com resposta"""
    i = k = 0
    j = 1
    while k <= n:
        if k == n:
            return print(f'SIM, {n} está na sequência fibonacci!')
        k = i + j
        i = j
        j = k
    return print(f'NÃO, {n} não está na sequência fibonacci...')

if __name__ == '__main__':
    print('='*40)
    print('TESTANDO A SEQUENCIA FIBONACCI'.center(40))
    print('='*40)
    n = tratamento(input("Digite um número inteiro maio que zero: "))
    fibonacci(n)
