def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


operacoes = {
    "1": ("Adição", somar),
    "2": ("Subtração", subtrair),
    "3": ("Multiplicação", multiplicar),
    "4": ("Divisão", dividir),
}

while True:
    print("\nCALCULADORA EM PYTHON")
    for codigo, (nome, _) in operacoes.items():
        print(f"{codigo} - {nome}")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ").strip()

    if escolha == "0":
        print("Calculadora encerrada.")
        break

    if escolha not in operacoes:
        print("Opção inválida.")
        continue

    try:
        numero_1 = float(input("Digite o primeiro número: "))
        numero_2 = float(input("Digite o segundo número: "))
        nome, funcao = operacoes[escolha]
        resultado = funcao(numero_1, numero_2)
        print(f"{nome}: {resultado:g}")
    except ValueError as erro:
        print(f"Erro: {erro}")
