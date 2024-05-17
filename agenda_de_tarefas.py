import os

def adicionar_tarefa(tarefa, arquivo):
    with open(arquivo, 'a') as f:
        f.write(tarefa + '\n')

def remover_tarefa(indice, arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    with open(arquivo, 'w') as f:
        for i, linha in enumerate(linhas):
            if i != indice:
                f.write(linha)

def visualizar_tarefa(arquivo):
    if not os.path.exists(arquivo) or os.path.getsize(arquivo) == 0:
        print("Ainda não há tarefas na agenda.")
    else:
        with open(arquivo, 'r') as f:
            tarefas = f.readlines()
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa.strip()}")

def main():
    arquivo = "tarefa.txt"

    while True:
        print("\n== Agenda de Tarefas ==")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Visualizar Tarefas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a tarefa que deseja adicionar: ")
            adicionar_tarefa(tarefa, arquivo)
            print("Tarefa adicionada .")
        elif escolha == "2":
            visualizar_tarefa(arquivo)
            indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
            remover_tarefa(indice, arquivo)
            print("Tarefa removida .")
        elif escolha == "3":
            visualizar_tarefa(arquivo)
        elif escolha == "4":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if _name_ == "_main_":
    main()
