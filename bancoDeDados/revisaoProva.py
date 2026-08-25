Questão 1 — 
Escreva o script SQL necessário para criar a estrutura inicial do banco de dados da loja: 
Crie o banco de dados com o nome db_techstore. 
Crie a tabela clientes contendo os campos: 
id_cliente (Chave Primária, inteiro, auto incremento) 
nome (texto, obrigatório) 
email (texto, único e obrigatório) 
Crie a tabela pedidos contendo os campos: 
id_pedido (Chave Primária, inteiro, auto incremento) 
data_pedido (data, obrigatório) valor_total (decimal/numeric) 
id_cliente (Chave Estrangeira que se relaciona com a tabela clientes)

CREATE DATABASE db_store;

USE db_store;

CREATE TABLE clientes(id INT PRIMARY KEY AUTO_INCREMENT,nome TEXT NOT NULL,email TEXT NOT NULL UNIQUE);

CREATE TABLE pedidos(id_pedidos INT PRIMARY KEY AUTO_INCREMENT,data_pedido DATE NOT NULL,id INT,CONSTRAINT fk_pedidos FOREIGN KEY (id) REFERENCES clientes(id));

Questão 2 — Manipulação de Dados (DML) 
Considerando as tabelas e o relacionamento criados na questão anterior, 
elabore os comandos SQL para realizar as seguintes operações: 
INSERT: Insira 2 novos registros na tabela clientes e, em seguida, 
insira 2 registros na tabela pedidos (sendo 1 pedido vinculado a cada um dos clientes cadastrados). 
UPDATE: Atualize o valor_total do pedido cujo id_pedido é igual a 1 para o valor 250.00. 
DELETE: Remova da tabela pedidos o registro em que o id_pedido seja igual a 2.

INSERT INTO clientes (nome,email) VALUES ("lucas","email@gmail");
INSERT INTO clientes (nome,email) VALUES ("caio","emailsad@gmail");

SELECT * FROM pedidos;

INSERT INTO pedidos (id,total_pedidos,data_pedido) VALUES (1,"90","2026-08-01");
INSERT INTO pedidos (id,total_pedidos,data_pedido) VALUES (2,"140,00","2026-08-01");

ALTER TABLE pedidos ADD total_pedidos FLOAT NOT NULL;

SELECT data_pedido, total_pedidos FROM pedidos WHERE total_pedidos < 100.00 ORDER BY total_pedidos ASC;

SELECT clientes.nome, pedidos.total_pedidos FROM clientes INNER JOIN pedidos ON clientes.id = pedidos.id;

Questão 3 — Controle de Dados (DCL) A equipe de atendimento ao cliente da TechStore precisa 
consultar dados cadastrais para prestar suporte, mas não deve ter acesso a dados 
financeiros nem permissão para alterar informações no banco. 
Escreva o script SQL para: 
Criar um novo usuário no banco de dados chamado 
atendente_suporte (com a senha 'Suporte@2026'). 
Conceder a esse usuário exclusivamente a permissão de leitura (SELECT) na tabela clientes.
DEPOIS DELETE O USUARIO, AS TABELAS E O BANCO

CREATE USER "Lucas"@"dev" IDENTIFIED "Suporte@2026";

GRANT SELECT ON db_store.clientes TO "Lucas"@"dev";

FLUSH PRIVILEGES;

DROP USER "Lucas"@"dev";

DROP DATABASE db_store;