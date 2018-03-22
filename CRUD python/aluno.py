#*-*coding: utf-8 *-*
import io
import sqlite3

class Aluno():
     
     nome = None
     idade = None
     curso = None 
     matricula = None 
      
     #construtor 
     def __init__(self, nome, idade,curso,matricula):
        self.nome = nome
        self.idade = idade
        self.curso = curso 
        self.matricula = matricula 
     
     #gets 

     def get_nome(self):
     	return self.nome

     def get_idade(self):
     	return self.idade

     def get_curso(self):
     	return self.curso

     def get_matricula(self):
     	return self.matricula

     #sets 
     def set_nome(self,n):
     	self.nome = n

     def set_idade(self,id):
     	self.idade = id

     def set_curso(self,c):
     	self.curso = c
     
     def set_matricula(self,m):
     	self.matricula = m
    
    #Funcoes do CRUD  utilizando sqlite
     def criar_tabela(self):
        # conectando...
        conn = sqlite3.connect('alunos.db')
        # definindo um cursor
        cur = conn.cursor()

        # criando a tabela (schema)
        cur.execute("""
        CREATE TABLE alunos (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                curso TEXT NOT NULL,
                mat INTEGER
        );
        """)
       
        print('Tabela criada com sucesso.')
        # desconectando...
        conn.close()
     
     def cadastrar(self):
        conn = sqlite3.connect('alunos.db')
        cur = conn.cursor()

        # inserindo dados na tabela
        cur.execute("""
        INSERT INTO alunos(nome, idade, curso, mat)
        VALUES (?,?,?,?)
        """,(self.get_nome(),self.get_idade(),self.get_curso(),self.get_matricula()))

        conn.commit()
        print('Dados inseridos com sucesso.')
        conn.close()

     def ler(self):
        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT * FROM alunos;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()

     def editar(self,id_aluno,novo_curso):
        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()

        # alterando os dados da tabela
        cursor.execute("""
        UPDATE alunos
        SET curso = ?
        WHERE id = ?
        """, (novo_curso, id_aluno))

        conn.commit()

        print('Dados atualizados com sucesso.')

        conn.close()
     def remover(self,id_aluno):
        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()

        # excluindo um registro da tabela
        cursor.execute("""
        DELETE FROM alunos
        WHERE id = ?
        """, (id_aluno,))

        conn.commit()

        print('Registro excluido com sucesso.')

        conn.close()
