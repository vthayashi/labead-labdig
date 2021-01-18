# ====================================================================
# Funcoes para interacao com o terminal do Blynk
# ====================================================================
import requests
import time

def limpa_terminal(site):
# Limpa o terminal no servidor na nuvem do Blynk enviando "clr"
# OBS: nao limpa a tela do terminal que o usuario enxerga no aplicativo
# Entradas:
#	site  - http request do Blynk para escrita no terminal
	r = requests.get(site + "clr")

def le_terminal(site, db):
# Le dados do terminal do Blynk
# Entradas:
# 	site - http request do Blynk para leitura do terminal
#   db   - Depuracao. Se db = 1, printa mensagens tambem no terminal da maquina remota
# Saidas:
#   text - novo texto lido do terminal

	r = requests.get(site)
	comprimento = len(r.json())

	while len(r.json()) == comprimento:
		r = requests.get(site)        
		time.sleep(1)

	if db == 1:
		print("> " + r.json()[-1])
	return r.json()[-1]		# Retorna o ultimo item da lista do JSON, ou seja, o ultimo dado recebido

def escreve_terminal(site, frase, db):
# Escreve uma frase no terminal do Blynk	
# Entradas:
#	site  - http request do Blynk para escrita no terminal
#	frase - frase a ser escrita no terminal
#   db    - Depuracao. Se db = 1, printa no terminal da maquina remota
	r = requests.get(site + frase + "\n")
	limpa_terminal(site)
	if db == 1:
		print(frase)

# Algumas constantes para uso nos outros arquivos:
# 	auth_token - token de autenticacao do projeto no Blynk
# 	termpin    - pino virtual onde esta mapeado o terminal do Blynk
#	termget    - http request para fazer get (ler) no terminal do Blynk
#	termupdate - http request para fezer update (escrever) no terminal do Blynk
#	db		   - Variavel de depuracao da funcao escreve_terminal
auth_token = "A2d3RGwoPfdfVMIAelKNz3_tzrodyBSd"
termpin    = "V0"
termget    = "http://blynk-cloud.com/" + auth_token + "/get/" + termpin
termupdate = "http://blynk-cloud.com/" + auth_token + "/update/" + termpin + "?value="
db         = 1		