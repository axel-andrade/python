#*-*coding: utf-8 *-*

import io
import sqlite3 
import os

from aluno import Aluno

def main():

	A = Aluno(None,None,None,None) #objeto vazio
	#A.criar_tabela() #criando o banco de dados e a tabela
    
	while True:

		op = input("\nOpcoes\n\n1-Cadastrar\n2-Ler\n3-Editar\n4-Deletar\n\nDigite a opcao: ")

		if(op==1): #CADASTRANDO ALUNO
            
			n = raw_input("Digite o nome: ")
			id = input("Digite a idade: ")
			curso = raw_input("Digite o curso: ")
			mat = input("Digite a matricula: ")

			A.set_nome(n)
			A.set_idade(id)
			A.set_curso(curso)
			A.set_matricula(mat) 
			os.system('clear') 
			A.cadastrar()
			
		elif(op==2): #LENDO ALUNO 
		     os.system('clear') 
		     A.ler()

		elif(op==3): #EDITANDO ALUNO 
			 id_aluno = raw_input("Digite o id do aluno para ser editado: ")
			 novo_curso = raw_input("Digite o novo curso do aluno: ")
			 os.system('clear') 
			 A.editar(id_aluno,novo_curso)

		elif(op==4): #REMOVENDO ALUNO
		     os.system('clear') 
		     id_aluno = raw_input("Digite o id do aluno a ser removido: ")
		     os.system('clear') 
		     A.remover(id_aluno)

		else:
			print "Opcao Invalido.\n"
			break


if(__name__ == "__main__"):
    main()
