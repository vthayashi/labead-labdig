# ====================================================================
# Script para montar o arquivo de pinagem
# ====================================================================
import requests
import time
import os
from terminal import *

escreve_terminal(termupdate, "Digite o nome do arquivo para a pinagem", db)
text = le_terminal(termget, db);

f1 = open(text + ".txt", "w")
escreve_terminal(termupdate, text + ".txt foi aberto", db)

escreve_terminal(termupdate, "Digite 'adicionar' ou 'a' para adicionar uma pinagem", db)
escreve_terminal(termupdate, "Digite 'finalizar' ou 'f' para finalizar o processo", db)

while(True):
    text = le_terminal(termget, db);

    if text == "adicionar" or text == "a":
        escreve_terminal(termupdate, "Digite o nome da entrada/saida", db)
        sinal = le_terminal(termget, db);

        escreve_terminal(termupdate, "Digite o nome do pino (escrever por exemplo AA2 ao inves de PIN_AA2", db)
        pino = le_terminal(termget, db);

        f1.write(sinal + " PIN_" + pino + "\n")
        escreve_terminal(termupdate, sinal + " PIN_" + pino + "     foi adicionado ao arquivo", db)

        escreve_terminal(termupdate, "Digite 'adicionar' para adicionar uma pinagem ou 'finalizar' para finalizar o processo", db)

    elif text == "finalizar" or text == "f":
        break

    else:
        escreve_terminal(termupdate, "Comando invalido. Digite 'adicionar' ou 'a' para adicionar uma pinagem ou 'finalizar' ou 'f' para finalizar o processo", db)

f1.close()
escreve_terminal(termupdate, "A criacao do arquivo de pinagem foi finalizada", db)