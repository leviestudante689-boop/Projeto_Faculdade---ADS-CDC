#Criando lista global de tarefas 

tarefas = ["felipe", "levi", "gustavo"]   # lista global — começa vazia

#Função de cadastro de aluno na academia

def cadastrar_aluno(nome, idade, dias_da_semana, objetivo, modalidade):
    novo_id = len(tarefas) + 1
    aluno = {
        "id": novo_id,
        "nome": nome,
        "modalidade": modalidade,
        "dias_semana": dias_da_semana,
        "objetivo": objetivo,
        "status": "Ativo",
        "sessoes": [],
        "checkins": []
    }
    tarefas.append(aluno)    # adiciona ao fim
    return aluno

#criando o dicionario   

def listar_alunos():
    for alunos in tarefas:
        print(alunos)

#adicionar na lista os alunos cadastrados

def adicionari_aluno(nome):
    for aluno in tarefas:
        if aluno['nome'] == nome:
            tarefas.remove (aluno)

#exibir sucesso 

def exibir_aluno_cadastrado(nome):
    for aluno in tarefas:
        if aluno['nome'] == nome:
            print(f"Aluno {nome} cadastrado com sucesso!")
            return
