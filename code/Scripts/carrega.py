# ====================================================================
# Script para carregar projeto do Quartus na placa FPGA
# ====================================================================
import os
import sys
import shutil
from terminal import *

# Definicao dos pinos de entrada e saida para verificacao antes da carga do sof

# entradas podem ser apenas os pinos GPIO_0 ou entao os pinos de clock da placa
entradas = ["N16", "B16", "M16", "C16", "D17", "K20", "K21", "K22", "M20", "M21",
            "N21", "R22", "R21", "T22", "N20", "N19", "M22", "P19", "L22", "P17",
            "P16", "M18", "L18", "L17", "L19", "K17", "K19", "P18", "R15", "R17",
            "R16", "T20", "T19", "T18", "T17", "T15",
            "M9", "H13", "E10", "V15"]

# saidas podem ser os pinos GPIO_1, leds ou displays de 7 segmentos
saidas   = ["H16", "A12", "H15", "B12", "A13", "B13", "C13", "D13", "G18", "G17",
            "H18", "J18", "J19", "G11", "H10", "J11", "H14", "A15", "J13", "L8",
            "A14", "B15", "C15", "E14", "E15", "E16", "F14", "F15", "F13", "F12",
            "G16", "G15", "G13", "G12", "J17", "K16",
            "AA2", "AA1", "W2", "Y3", "N2", "N1", "U2", "U1", "L2", "L1",
            "U21", "V21", "W22", "W21", "Y22", "Y21", "AA22", 
            "AA20", "AB20", "AA19", "AA18", "AB18", "AA17", "U22",
            "Y19", "AB17", "AA10", "Y14", "V14", "AB22", "AB21",
            "Y16", "W16", "Y17", "V16", "U17", "V18", "V19",
            "U20", "Y20", "V20", "U16", "U15", "Y15", "P9",
            "N9", "M8", "T14", "P14", "C1", "C2", "W19"]

# ====================================================================
# Inicializacao
# ====================================================================
if len(sys.argv) != 3:
    escreve_terminal(termupdate, "O numero de agumentos eh invalido!", db)
    escreve_terminal(termupdate, "O script devera ser executado como:", db)
    escreve_terminal(termupdate, "       python carrega.py expXX nome_do_projeto", db)
    sys.exit()
    
exp     = sys.argv[1]   # Numero da experiencia
projeto = sys.argv[2]   # Nome do projeto

try:
    os.chdir(exp)  
except OSError as e:
    escreve_terminal(termupdate, "Voce esta tentando carregar o projeto antes de compila-lo", db)
    sys.exit()

# Descoberta do nome do projeto (pode ser diferente do nome do qar)
for arquivo in os.listdir():
    if arquivo.endswith(".qsf"):
        projeto = arquivo.split(".")[0]
               
# =====================================================================
# Verificacao adicional da pinagem antes da carga do executavel
# ====================================================================
escreve_terminal(termupdate, "Comecando a verificacao dos pinos antes da carga do executavel na placa", db)

try:
    f = open("output_files/" + projeto + ".pin", "r")
except OSError as e:
    escreve_terminal(termupdate, "Voce esta tentando carregar o projeto antes de compila-lo", db)
    sys.exit()

linhas = f.readlines()

for linha in linhas:
    dado = linha.split(" ")
    dado = [x for x in dado if x != ""] # Remocao de todos os espacos restantes da lista
    if "Y" in dado:                     # Linha indicando pinagem feita pelo usuario
        if dado[4] == "output":
            if not(dado[2] in saidas):
                escreve_terminal(termupdate, "PIN_" + dado[2] + " nao eh uma saida valida", db)
                sys.exit()

        elif dado[4] == "input":
            if not(dado[2] in entradas):
                escreve_terminal(termupdate, "PIN_" + dado[2] + " nao eh uma entrada valida", db)
                sys.exit()

f.close()

escreve_terminal(termupdate, "Os pinos estao corretos. Parabens por nao fazer uma besteira", db)

# ====================================================================
# Carga do executavel (.sof) na placa FPGA
# ====================================================================
escreve_terminal(termupdate, "Carregando arquivo sof na placa FPGA", db)

comando = "quartus_pgm -c usb-blaster -m JTAG -o p;output_files/" + projeto + ".sof"

if os.system(comando) != 3:
    escreve_terminal(termupdate, "O arquivo sof for carregado com sucesso", db)
else:
    escreve_terminal(termupdate, "Erro na carga do arquivo sof", db)
    sys.exit()