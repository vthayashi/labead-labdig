# ====================================================================
# Script para verificar/alterar a baud rate do script do ESP8266
# ====================================================================

import os
import sys
from terminal import *

escreve_terminal(termupdate, "Verificando o valor atual da baudrate", db)

# Verifica o valor do baudrare
try:
    f1 = open("ESP8266_Standalone/ESP8266_Standalone.ino", "r")
except OSError as e:
    escreve_terminal(termupdate, "Script do ESP8266 nao encontrado", db)
    sys.exit(2)
    
linhas = f1.readlines()
f1.close()

for linha in linhas:
    if "mySerial.begin" in linha:                          # '  mySerial.begin(X);'
        dado = linha.replace("(", " ").replace(")", " ")   # '  mySerial.begin X ;'
        dado = dado.split(" ")                             # ['', '', 'mySerial.begin, 'X', ';']
        dado = [x for x in dado if x != ""]                # 'mySerial.begin', 'X', ';']
        dado = dado[1]                                     # 'X'

escreve_terminal(termupdate, "BaudRate = " + dado, db)
escreve_terminal(termupdate, "Digite 's' para mudar o valor da baudrate ou 'n' para voltar ao menu" , db)
opcao = le_terminal(termget, db);   

while opcao != "s" and opcao != "n":
    escreve_terminal(termupdate, "Opcao invalida!" , db)
    escreve_terminal(termupdate, "Digite 's' para mudar o valor da baudrate ou 'n' para voltar ao menu" , db)    
    opcao = le_terminal(termget, db); 
    
# Altera o valor do baudrate
if opcao == "s":
    escreve_terminal(termupdate, "Digite o valor da baudrate" , db)
    baudrate = le_terminal(termget, db);

    f1 = open("ESP8266_Standalone/ESP8266_Standalone.ino", "w")

    for linha in linhas:
        if "mySerial.begin" in linha:
            f1.write("  mySerial.begin(" + baudrate + ");\n")
        else:
            f1.write(linha)  
    f1.close()
    escreve_terminal(termupdate, "Valor da baudrate alterado para " + baudrate , db)
    sys.exit(2)
