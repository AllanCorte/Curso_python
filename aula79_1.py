# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json


def listar(lista_tarefas):
    print()
    if not lista_tarefas:
        print('Não tem tarefas')
        return

    print('Tarefas:')
    for tarefa in lista_tarefas:
        print(f'\t{tarefa}')


def desfazer(lista_tarefas, tarefas_desfeitas):
    print()

    if not lista_tarefas:
        print('Não tem tarefas para desfazer')
        return

    tarefa = lista_tarefas.pop()
    print(f'{tarefa} foi desfeita')
    tarefas_desfeitas.append(tarefa)
    print()
    listar(lista_tarefas)


def refazer(lista_tarefas, tarefas_desfeitas):
    print()
    if not tarefas_desfeitas:
        print('Não tem tarefas para refazer')
        return

    tarefa = tarefas_desfeitas.pop()
    print(f'{tarefa} foi refeita')
    lista_tarefas.append(tarefa)
    print()
    listar(lista_tarefas)


def adicionar(tarefa, lista_tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return

    print(f'{tarefa}: adicionada com sucesso')
    lista_tarefas.append(tarefa)
    print()
    listar(lista_tarefas)


def ler(lista_tarefas, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print('Arquivo não existe, criando novo arquivo...')
        salvar(lista_tarefas, caminho_arquivo)
    except json.JSONDecodeError:
        print('Arquivo corrompido ou vazio, iniciando lista vazia.')
    return []


def salvar(lista_tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=2, ensure_ascii=False)


caminho_arquivo = 'aula79.json'

lista_tarefas = ler([], caminho_arquivo)
tarefas_desfeitas: list[str] = []

while True:
    print('Comandos: desfazer, refazer, listar, sair')
    comando = input('Digite uma tarefa ou um comando: ').strip()

    if comando == 'desfazer':
        desfazer(lista_tarefas, tarefas_desfeitas)
    elif comando == 'refazer':
        refazer(lista_tarefas, tarefas_desfeitas)
    elif comando == 'listar':
        listar(lista_tarefas)
    elif comando == 'sair':
        break
    else:
        adicionar(comando, lista_tarefas)
    salvar(lista_tarefas, caminho_arquivo)
