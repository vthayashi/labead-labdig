# ====================================================================
# Script para alterar os valores dos pinos virtuais do Blynk
# ====================================================================
import requests
import os
from terminal import *

escreve_terminal(termupdate, "Digite o nome do pino seguido de espaco e o seu valor para alterar a entrada", db)
escreve_terminal(termupdate, "Ex: E1 1 ou E1 0", db)
escreve_terminal(termupdate, "Caso queira voltar ao menu do script, digite 'sair' ou 's' ", db)

while(True):
	text = le_terminal(termget, db);

	if text == "sair" or text == "s":
		break

escreve_terminal(termupdate, "Fim dos testes", db)