import mysql.connector
from mysql.connector import Error

#CREATE DATABASE gestao_estoque;

#CREATE TABLE produtos (id INT AUTO_INCREMENT PRIMARY KEY,
#nome VARCHAR(100) NOT NULL,
#quantidade INT NOT NULL,
#preco DECIMAL (10,2) NOT NULL);

#INSERT INTO produtos (nome,quantidade,preco) VALUES ('Arroz',10,5.99);

db_config = {
    'host' : 'localhost',
    'database' : 'gestao_estoque',
    'user' : 'root',
    'password' : '13062003'
}

conexao = mysql.connector.connect(**db_config)

cursor = conexao.cursor()

def inserir_itens():
    nome = input("Insira o nome do produto:")
    quantidade = int(input("Insira a quantidade de itens no estoque:"))
    preco = float(input("Insira o preco da Un / Pc / Vl:"))

    sql = "INSERT INTO produtos (nome,quantidade,peco) VALUES (%s,%s,%s);"
    cursor.execute(sql, (nome,quantidade,preco))
    conexao.commit()

def estoque_low():
    sql = "SELECT * FROM produtos WHERE quantidade <11 ;" 
    cursor.execute(sql)
    conexao.commit()

def atualizar_preco ():
    idAtualizar = int(input("Digite o id do produto que deseja o preço:"))
    pecoAtualizar = float(input("Digite o novo preço do produto:"))

    sql = "UPDATE produtos SET preco = %s id = %s;"
    cursor.execute(sql, (pecoAtualizar,idAtualizar))
    conexao.commit()


while True:

    print("1 - Inserir itens:")
    print("2 - Mostrar itens com estoque baixo:")
    print("3 - Atualizar preço de um item:")
    print("0 - Sair")

    op = int(input("Digite a opção desejada:"))
    match op:
        case 1:
            inserir_itens()
        case 2:
            estoque_low()
        case 3:
            atualizar_preco()
        case 0:
            cursor.close()
            conexao.close()
            break
            

#Sistema de Gestão de Estoque

#Objetivo: Criar um script em Python que conecte ao MySQL local, crie um banco de dados, defina uma tabela de produtos e execute operações básicas de inserção e consulta.

#Requisitos

#Estrutura do Banco de Dados:
#1 - Crie um banco de dados chamado gestao_estoque.
#2 - Crie uma tabela produtos com os seguintes campos:
#id: chave primária, inteiro, auto incremento.
#nome: texto (VARCHAR 100), não nulo.
#quantidade: inteiro, não nulo.
#preco: decimal (10, 2), não nulo.

#Funcionalidades do Script Python:
#Conexão: Conectar ao MySQL local (localhost, usuário e senha do WSL).
#Criação Automática: Executar comandos SQL para criar o banco de dados e a tabela caso ainda não existam (CREATE DATABASE IF NOT EXISTS, CREATE TABLE IF NOT EXISTS).
#1 - Inserção de Dados: Inserir 4 produtos no banco via script (usando placeholders %s para prevenir SQL Injection).
#2 - Consulta Filtro: Buscar e exibir no terminal apenas os produtos cuja quantidade seja menor que 10 unidades (alerta de estoque baixo).
#3 - Atualização: Alterar o preço de um dos produtos e exibir a confirmação no terminal.
