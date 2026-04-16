# app.py
tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa {tarefa} adicionada!")
def listar_tarefas():
    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}.")

# Uso da aplicação
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Criar código simples")
listar_tarefas()

#camilla passou por aqui 
