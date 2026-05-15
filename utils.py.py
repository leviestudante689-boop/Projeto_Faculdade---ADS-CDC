# Criando funções auxiliares usadas no sistema da academia

def titulo(texto):
    print("\n" + "=" * 40)  # Mostra tanto o título quanto a as linhas superiores e inferiores, assim deixando mais organizado visualmente, podemos dizer assim

    print(texto.upper())    
    print("=" * 40)        


def linha():
    print("-" * 40)   # separador simples, mais para separar os dados em si, não tem muito segredo não :)


def ler_nome():
    nome = input("Digite o nome do aluno: ")  # pede o nome do aluno basicamente
    return nome


def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))  # tenta converter pra número, transforma oque o usuário digitou em um número inteiro
            return idade
        except:
            print("Idade inválida, digite um número.")


def ler_texto(msg):
    texto = input(msg)  # leitura simples de texto, lê qualquer texto, literalmente é só isso
    return texto


def pausar():
    input("\nPressione Enter para continuar...")  # pausa o sistema, o sistema espera a ação do usuário para continuar


def mostrar_alunos(lista):
    titulo("ALUNOS CADASTRADOS")
    for aluno in lista:
        print(f"ID: {aluno['id']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Modalidade: {aluno['modalidade']}")
        print(f"Objetivo: {aluno['objetivo']}")
        print(f"Status: {aluno['status']}")
        linha()

  # Bom, basicamente é um looping que percorre a lista e exibe os alunos cadastrados com suas informações
  # Assim imprimindo os dados de cada aluno da forma mais organizada possível, assim evitando confusões futuras
