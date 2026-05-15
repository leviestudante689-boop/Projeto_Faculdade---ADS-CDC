#Variavel gloval para armazenar os dados

lista_principal = [] #a lista é a lista basicamente dos alunos e tals, nao tem mt que falar nao

fifo_atendimento = [] # a fila em fifo pra controla a ordem de atendimento dos alunos, ou seja, o primeiro a chegar é o primeiro a ser atendido

lifo_sessoes = [] # a pilha em lifo para controlar as sessoes, ou seja, a ultima sessao a ser criada é a primeira a ser atendida!!!!!!!!!

#agora é as tuplas 

status_aluno = ("ativo", "inativo", "pendente") 

status_prioridade = ("alta", "media", "baixa")

#Aqui foi usado as listas para armazenar dados, sendo a dados.py onde ta as variveis globais
#alem disso usamos lifo, fifo e tuplas pra organiza tudo direitnho e nao haver colapso do sistema
