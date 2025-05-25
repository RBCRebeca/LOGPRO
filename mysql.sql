-- Criação do banco de dados
CREATE DATABASE sistema_locacao;
USE cantinho_ideal;

-- Tabela de clientes
CREATE TABLE IF NOT EXISTS cliente (
    id_cli INT AUTO_INCREMENT PRIMARY KEY,
    cli_nome VARCHAR(255) NOT NULL,
    cli_cpf VARCHAR(14) UNIQUE NOT NULL,
    cli_email VARCHAR(255),
    cli_telefone VARCHAR(20)
);

-- Tabela de imóveis
CREATE TABLE IF NOT EXISTS imovel (
    id_imovel INT AUTO_INCREMENT PRIMARY KEY,
    im_estado VARCHAR(100),
    im_cidade VARCHAR(100),
    im_rua VARCHAR(255),
    im_cep VARCHAR(9),
    im_numero VARCHAR(10),
    im_valor_aluguel DECIMAL(10, 2),
    im_apartamento BOOLEAN DEFAULT FALSE,
    im_casa BOOLEAN DEFAULT FALSE,
    im_chale BOOLEAN DEFAULT FALSE
);

-- Tabela de solicitações de locação
CREATE TABLE IF NOT EXISTS solicitacao_locacao (
    id_sl INT AUTO_INCREMENT PRIMARY KEY,
    id_solicitacao VARCHAR(50) UNIQUE,
    id_contrato VARCHAR(50),
    id_imovel INT,
    id_inquilino INT,
    data_inicio DATE,
    data_fim DATE,
    valor_mensal DECIMAL(10, 2),
    status_aluguel ENUM('ativo', 'encerrado'),
    status_solicitacao ENUM('pendente', 'aprovada', 'recusada'),
    FOREIGN KEY (id_imovel) REFERENCES imovel(id_imovel),
    FOREIGN KEY (id_inquilino) REFERENCES cliente(id_cli)
);

-- Inserindo clientes de exemplo
INSERT INTO cliente (cli_nome, cli_cpf, cli_email, cli_telefone) VALUES
('Maria Oliveira', '123.456.789-00', 'maria@gmail.com', '(11) 99999-1234'),
('João Silva', '987.654.321-00', 'joao@gmail.com', '(21) 98888-5678');

-- Inserindo imóveis de exemplo
INSERT INTO imovel (im_estado, im_cidade, im_rua, im_cep, im_numero, im_valor_aluguel, im_apartamento, im_casa, im_chale) VALUES
('SP', 'São Paulo', 'Av. Paulista', '01311-000', '1000', 2500.00, TRUE, FALSE, FALSE),
('RJ', 'Rio de Janeiro', 'Rua das Laranjeiras', '22240-003', '200', 1800.00, FALSE, TRUE, FALSE);

-- Inserindo solicitações de locação de exemplo
INSERT INTO solicitacao_locacao (
    id_solicitacao, id_contrato, id_imovel, id_inquilino, data_inicio, data_fim, valor_mensal, status_aluguel, status_solicitacao
) VALUES
('SOL123', 'CONT001', 1, 1, '2025-06-01', '2026-06-01', 2500.00, 'ativo', 'aprovada'),
('SOL124', 'CONT002', 2, 2, '2025-07-01', '2026-07-01', 1800.00, 'pendente', 'pendente');

-- Exemplo de consulta com JOIN para visualizar as locações
SELECT 
    sl.id_solicitacao,
    c.cli_nome,
    i.im_cidade,
    i.im_valor_aluguel,
    sl.data_inicio,
    sl.data_fim,
    sl.status_aluguel,
    sl.status_solicitacao
FROM solicitacao_locacao sl
JOIN cliente c ON sl.id_inquilino = c.id_cli
JOIN imovel i ON sl.id_imovel = i.id_imovel;
