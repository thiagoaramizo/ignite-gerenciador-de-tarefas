"""Projeto: Gerenciador de tarefas
   Autor: Thiago Aramizo
"""

def adicionar_tarefa(nome_tarefa, lista_tarefas):
  tarefa = {
    "nome": nome_tarefa,
    "completada": False
  }
  lista_tarefas.append( tarefa )
  print(f"\nTarefa '{nome_tarefa}' foi adicionada com sucesso!")
  return

def ver_tarefas(lista_tarefas):
  print("\nLista de Tarefas:")
  for indice, tarefa in enumerate(lista_tarefas, start=1):
    status = "ok" if tarefa['completada'] else " "
    print(f"{indice}. [{status}] {tarefa['nome']}")
  return


def atualizar_tarefa(lista_tarefas, indice_tarefa, nome_tarefa):
  indice_tarefa_tratado = int(indice_tarefa) - 1

  if indice_tarefa_tratado < 0 or indice_tarefa_tratado >= len(lista_tarefas):
    print(f"\nErro: Tarefa não encontrada.")
  else:
    lista_tarefas[indice_tarefa_tratado]["nome"] = nome_tarefa
    print(f"\nTarefa {indice_tarefa} alterada com sucesso!")
  return

def concluir_tarefa(lista_tarefas, indice_tarefa):
  indice_tarefa_tratado = int(indice_tarefa) - 1

  if indice_tarefa_tratado < 0 or indice_tarefa_tratado >= len(lista_tarefas):
    print(f"\nErro: Tarefa não encontrada.")
  else:
    lista_tarefas[indice_tarefa_tratado]["completada"] = True
    print(f"\nTarefa {indice_tarefa} concluída com sucesso!")
  return

def deletar_concluidas(lista_tarefas):
  for indice, tarefa in enumerate(lista_tarefas):
    if tarefa["completada"]:
      lista_tarefas.pop(indice)
  print("\nTarefas concluídas removidas com sucesso!")
  return

tarefas = []

while True:
  print("\nMenu do Gerenciador de Tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a opção: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa: ")
    adicionar_tarefa(nome_tarefa, tarefas)

  elif escolha == "2":
    ver_tarefas(tarefas)
  
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("Informe o número da tarefa a ser alterada: ")
    nome_tarefa = input("Digite o novo nome da tarefa: ")
    atualizar_tarefa(tarefas, indice_tarefa, nome_tarefa)

  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("Informe o número da tarefa a ser concluída: ")
    concluir_tarefa(tarefas, indice_tarefa)

  elif escolha == "5":
    deletar_concluidas(tarefas)

  elif escolha == "6":
    break

  else:
    print("Opção inválida.")