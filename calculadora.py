import math

def calculadora():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Potência")
        print("6 - Raiz quadrada")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Calculadora encerrada!")
            break

        if opcao not in ["1", "2", "3", "4", "5", "6"]:
            print("Opção inválida!")
            continue

        try:
            a = float(input("Digite o primeiro número: "))

            if opcao != "6":
                b = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = a + b

            elif opcao == "2":
                resultado = a - b

            elif opcao == "3":
                resultado = a * b

            elif opcao == "4":
                if b == 0:
                    print("Erro: divisão por zero!")
                    continue
                resultado = a / b

            elif opcao == "5":
                resultado = a ** b

            elif opcao == "6":
                if a < 0:
                    print("Erro: número negativo!")
                    continue
                resultado = math.sqrt(a)

            print(f"\nResultado: {resultado}")

        except ValueError:
            print("Erro: digite um número válido!")
        except (OverflowError, ZeroDivisionError):
            print("Erro matemático!")

calculadora()