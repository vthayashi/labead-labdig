# ====================================================================
# Script para compilar e carregar script do ESP8266
# ====================================================================
# 1 eh o codigo de erro retornado pelo os.system() caso ambos os comandos do arduino-cli deem errado
# sys.exit() ira retornar 2 na chamada os.system() do main.py indicando erro na execucao
import os
import sys
from terminal import *

escreve_terminal(termupdate, "Comencando processo de compilacao e carga do script do ESP8266", db)

# Altera o valor do token de autenticacao no script do esp8266
try:
    f1 = open("ESP8266_Standalone/ESP8266_Standalone.ino", "r")
except OSError as e:
    escreve_terminal(termupdate, "Script do ESP8266 nao encontrado", db)
    sys.exit(2)
    
linhas = f1.readlines()
f1.close()

f1 = open("ESP8266_Standalone/ESP8266_Standalone.ino", "w")
for linha in linhas:
    if "auth[]" in linha:
        texto = 'char auth[] = "' + auth_token + '";\n'
        f1.write(texto)
    else:
        f1.write(linha)
f1.close()

# Compila o script
if os.system("arduino-cli compile --fqbn esp8266:esp8266:nodemcuv2 ESP8266_Standalone") != 1:
    escreve_terminal(termupdate, "O script do ESP8266 foi compilado com sucesso", db) 
else:
    escreve_terminal(termupdate, "Erro no processo de compilacao do script do ESP8266", db) 
    sys.exit(2)
    
# Localiza a porta COM que esta conectada ao ESP8266
os.system("arduino-cli board list > log.txt")
f1 = open("log.txt", "r")
linhas = f1.readlines()
linha = linhas[2]
porta = linha.split(" ")[0]
f1.close()
os.remove("log.txt")

escreve_terminal(termupdate, "A porta identificada do ESP8266 foi a " + porta, db)

# Carrega o script
if os.system("arduino-cli upload -p " + porta + " --fqbn esp8266:esp8266:nodemcuv2 ESP8266_Standalone") != 1:
    escreve_terminal(termupdate, "O script do ESP8266 foi carregado com sucesso", db) 
else:
    escreve_terminal(termupdate, "Erro no processo de carga do script do ESP8266", db) 
    sys.exit(2)