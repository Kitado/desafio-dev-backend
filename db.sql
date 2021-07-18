CREATE DATABASE `Blu365` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

CREATE TABLE Blu365.profissoes (
	id INT auto_increment NOT NULL,
	profissao varchar(100) NOT NULL,
	valor_diario DECIMAL(10, 2) NOT NULL,
	CONSTRAINT profissoes_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_general_ci;
