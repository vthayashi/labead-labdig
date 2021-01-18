# ====================================================================
# Funcoes para interacao com o diretorio
# ====================================================================
import os
import shutil
from terminal import *

arquivos = ["ESP8266_Standalone", "arduino.py", "carrega.py", "compila.py", "diretorio.py", 
            "main.py", "pinagem.py", "terminal.py", "testa.py", "baudrate.py", "__pycache__"]

def mostra_diretorio():
# Mostra os arquivos presentes no diretorio com excecao dos definidos na lista "arquivos"
	for f in os.listdir():
		if not(f in arquivos):
			escreve_terminal(termupdate, f, db)

def remove_arquivo(arquivo):
# Remove um arquivo/diretorio com excecao dos definidos na lista "arquivos"
# Entradas:
#	arquivo  - arquivo/diretorio a ser removido
	if not(arquivo in arquivos):
		if "." in arquivo:
			escreve_terminal(termupdate, "Removendo arquivo " + arquivo, db)
			try:
				os.remove(arquivo)
			except OSError as e:
				escreve_terminal(termupdate, "Arquivo nao encontrado", db)

		else:
			escreve_terminal(termupdate, "Removendo diretorio " + arquivo, db)
			try:
				shutil.rmtree(arquivo)
				escreve_terminal(termupdate, "Diretorio removido com sucesso" , db)
			except OSError as e:
				escreve_terminal(termupdate, "Diretorio nao encontrado", db)
	else:
		escreve_terminal(termupdate, "Nome do arquivo/diretorio eh reservado", db)