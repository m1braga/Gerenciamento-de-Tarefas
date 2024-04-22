import json  # Importa o módulo json para lidar com dados em formato JSON
import os  # Importa o módulo os para interagir com o sistema operacional
from datetime import datetime  # Importa a classe datetime do módulo datetime

class GerenciadorDeTarefas:  # Define a classe GerenciadorDeTarefas para gerenciar tarefas
    def __init__(self):  # Método de inicialização da classe
        self.tarefas = []  # Inicializa uma lista vazia para armazenar as tarefas

    def adicionar_tarefas(self, titulo, descricao, prioridade, data):  # Método para adicionar uma nova tarefa
        tarefa = {  # Cria um dicionário para representar a tarefa
            'titulo': titulo,  # Título da tarefa
            'descricao': descricao,  # Descrição da tarefa
            'prioridade': prioridade,  # Prioridade da tarefa
            'data': data.strftime('%Y-%m-%d'),  # Data da tarefa formatada como string
            'concluido': False  # Indica se a tarefa está concluída ou não
        }
        self.tarefas.append(tarefa)  # Adiciona a tarefa à lista de tarefas

    def listar_tarefas(self):  # Método para listar as tarefas
        for idx, tarefa in enumerate(self.tarefas, 1):  # Percorre a lista de tarefas com um índice
            print(f"{idx}. {tarefa['titulo']} - prioridade: {tarefa['prioridade']} - data: {tarefa['data']}")  # Exibe as informações da tarefa

    def marcar_tarefa_concluido(self, tarefa_idx):  # Método para marcar uma tarefa como concluída
        if tarefa_idx >= 1 and tarefa_idx <= len(self.tarefas):  # Verifica se o índice da tarefa é válido
            self.tarefas[tarefa_idx - 1]['concluido'] = True  # Marca a tarefa como concluída
            print(f"Tarefa '{self.tarefas[tarefa_idx - 1]['titulo']}' marcada como concluída.")  # Exibe uma mensagem de confirmação
        else:
            print("Índice de tarefa inválido.")  # Exibe uma mensagem de erro se o índice da tarefa for inválido

    def salvar_tarefas(self, nome_do_arquivo='tarefas.json'):  # Método para salvar as tarefas em um arquivo JSON
        with open(nome_do_arquivo, 'w') as file:  # Abre o arquivo para escrita
            json.dump(self.tarefas, file)  # Serializa as tarefas em formato JSON e escreve no arquivo

    def carregar_tarefas(self, nome_do_arquivo='tarefas.json'):  # Método para carregar as tarefas de um arquivo JSON
        if os.path.exists(nome_do_arquivo):  # Verifica se o arquivo existe
            with open(nome_do_arquivo, 'r') as file:  # Abre o arquivo para leitura
                self.tarefas = json.load(file)  # Carrega as tarefas do arquivo JSON

def main():  # Função principal para interação com o usuário
    gerenciador_de_tarefas = GerenciadorDeTarefas()  # Cria uma instância da classe GerenciadorDeTarefas
    gerenciador_de_tarefas.carregar_tarefas()  # Carrega as tarefas existentes do arquivo JSON

    while True:  # Loop principal do programa
        print("\nMenu do Gerenciador de Tarefas:")  # Exibe o menu do gerenciador de tarefas
        print("1. Adicionar Tarefas")  # Opção para adicionar uma nova tarefa
        print("2. Listar Tarefas")  # Opção para listar as tarefas
        print("3. Marcar Tarefa Como Concluído")  # Opção para marcar uma tarefa como concluída
        print("4. Salvar Tarefa")  # Opção para salvar as tarefas em um arquivo JSON
        print("5. Sair")  # Opção para sair do programa

        escolha = input("Insira a opção desejada: ")  # Solicita ao usuário a escolha de uma opção

        if escolha == '1':  # Se a escolha for adicionar uma nova tarefa
            titulo = input("Insira o título da tarefa: ")  # Solicita o título da tarefa
            descricao = input("Insira a descrição da tarefa: ")  # Solicita a descrição da tarefa
            prioridade = input("Insira a prioridade da tarefa (Baixo/Médio/Alto): ").capitalize()  # Solicita a prioridade da tarefa
            data_str = input("Coloque a data (YYYY-MM-DD): ")  # Solicita a data da tarefa
            data = datetime.strptime(data_str, '%Y-%m-%d').date()  # Converte a data para o formato datetime.date
            gerenciador_de_tarefas.adicionar_tarefas(titulo, descricao, prioridade, data)  # Chama o método para adicionar a nova tarefa
        elif escolha == '2':  # Se a escolha for listar as tarefas
            gerenciador_de_tarefas.listar_tarefas()  # Chama o método para listar as tarefas
        elif escolha == '3':  # Se a escolha for marcar uma tarefa como concluída
            tarefa_idx = int(input("Insira o índice da tarefa para marcar como concluído: "))  # Solicita o índice da tarefa a ser marcada como concluída
            gerenciador_de_tarefas.marcar_tarefa_concluido(tarefa_idx)  # Chama o método para marcar a tarefa como concluída
        elif escolha == '4':  # Se a escolha for salvar as tarefas
            gerenciador_de_tarefas.salvar_tarefas()  # Chama o método para salvar as tarefas em um arquivo JSON
            print("Tarefas salvas em 'tarefas.json'.")  # Exibe uma mensagem de confirmação
        elif escolha == '5':  # Se a escolha for sair do programa
            gerenciador_de_tarefas.salvar_tarefas()  # Chama o método para salvar as tarefas em um arquivo JSON
            print("Tarefa salva. Saindo do programa.")  # Exibe uma mensagem de confirmação e sai do programa
            break  # Sai do loop principal
        else:  # Se a escolha for inválida
            print("Opção inválida. Tente novamente.")  # Exibe uma mensagem de erro

if __name__ == "__main__":  # Verifica se o programa está sendo executado diretamente
    main()  # Chama a função principal para iniciar o programa
