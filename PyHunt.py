from random import randint 

print("Bem Vindo ao PyNumHunt!")
dificuldade = input("Digite a dificuldade selecionada(fácil, médio, difícil ou insano): ").lower()
while True:
    if  dificuldade == "facil" or dificuldade == "fácil":
        numeroSorteado = randint(1,11)
        numero = int(input("Digite um número: "))
        while True:
            if numero < 1 or numero > 10:
                print("O número digitado não faz parte da dificuldade selecionada (1 até 10), tente novamente!")
                numero = int(input("Digite um número: "))
            elif numero < numeroSorteado: 
                print(f"Xiii, chutou baixo. dica o número sorteado é maior que {numero}")
                numero = int(input("Digite um número: "))
            elif numero > numeroSorteado:
                print(f"xiiii, chutou alto. dica: o número sorteado é menor que {numero}")
                numero = int(input("Digite um número: "))
            elif numero == numeroSorteado:
                print(f" Parabéns, você acertou! O número sorteado é {numero}")
                break

    elif dificuldade == "medio" or dificuldade == "médio":
        numeroSorteado = randint(1,51)
        numero = int(input("Digite um número: "))
        while True:
            if numero < 1 or numero > 50:
                print("O número digitado não faz parte da dificuldade selecionada (1 até 50), tente novamente!")
                numero = int(input("Digite um número: "))
            elif numero < numeroSorteado: 
                print(f"Xiii, chutou baixo. dica o número sorteado é maior que {numero}")
                numero = int(input("Digite um número: "))
            elif numero > numeroSorteado:
                print(f"xiiii, chutou alto. dica: o número sorteado é menor que {numero}")
                numero = int(input("Digite um número: "))
            elif numero == numeroSorteado:
                print(f" Parabéns, você acertou! O número sorteado é {numero}")
                break
    elif dificuldade == "dificil" or dificuldade == "difícil":
        numeroSorteado = randint(1,101)
        numero = int(input("Digite um número: "))
        while True:
            if numero < 1 or numero > 100:
                print("O número digitado não faz parte da dificuldade selecionada (1 até 100), tente novamente!")
                numero = int(input("Digite um número: "))
            elif numero < numeroSorteado: 
                print(f"Xiii, chutou baixo. dica o número sorteado é maior que {numero}")
                numero = int(input("Digite um número: "))
            elif numero > numeroSorteado:
                print(f"xiiii, chutou alto. dica: o número sorteado é menor que {numero}")
                numero = int(input("Digite um número: "))
            elif numero == numeroSorteado:
                print(f" Parabéns, você acertou! O número sorteado é {numero}")
                break
    elif dificuldade == "insano":
        numeroSorteado = randint(1,1001)
        numero = int(input("Digite um número: "))
        while True:
            if numero < 1 or numero > 1000:
                print("O número digitado não faz parte da dificuldade selecionada (1 até 1000), tente novamente!")
                numero = int(input("Digite um número: "))
            elif numero < numeroSorteado: 
                print(f"Xiii, chutou baixo. dica o número sorteado é maior que {numero}")
                numero = int(input("Digite um número: "))
            elif numero > numeroSorteado:
                print(f"xiiii, chutou alto. dica: o número sorteado é menor que {numero}")
                numero = int(input("Digite um número: "))
            elif numero == numeroSorteado:
                print(f" Parabéns, você acertou! O número sorteado é {numero}")
                break
    else: 
        print("Dificuldade inválida. Insira a seguir Facil, Medio, Dificil ou Insano")
        dificuldade = input("Digite a dificuldade selecionada(fácil, médio, difícil ou insano): ").lower()

