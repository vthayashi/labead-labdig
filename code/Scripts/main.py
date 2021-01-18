# ====================================================================
# Script top
# ====================================================================
import requests
import os
import gdown
from terminal import *
from diretorio import *

def menu(site):
    escreve_terminal(site, "==========================================================================", db)
    escreve_terminal(site, "Bem vindo ao script do LabEAD", db)
    escreve_terminal(site, "==========================================================================", db)
    escreve_terminal(site, "Digite 'carregar' ou 'ca' para carregar um projeto na placa FPGA", db)
    escreve_terminal(site, "Digite 'compilar' ou 'co' para compilar um projeto qar", db)
    escreve_terminal(site, "Digite 'esp8266'  ou 'es' para carregar o script no esp8266", db)
    escreve_terminal(site, "Digite 'testar'   ou 't'  para alterar os valores das entradas pelo terminal", db)
    escreve_terminal(site, "Digite 'pinar'    ou 'pi' para montar um arquivo de pinagem", db)
    escreve_terminal(site, "Digite 'exp'      ou 'e'  para mudar o nome da experiencia", db)
    escreve_terminal(site, "Digite 'projeto'  ou 'pr' para mudar o nome do projeto", db)
    escreve_terminal(site, "Digite 'baixar'   ou 'b'  para baixar um qar do Google Drive", db)
    escreve_terminal(site, "Digite 'mostrar'  ou 'm'  para mostrar o nome atual da experiencia/projeto", db)
    escreve_terminal(site, "Digite 'arquivos' ou 'ar' para mostrar os arquivos/diretorios da pasta", db)
    escreve_terminal(site, "Digite 'remover'  ou 'r'  para remover um arquivo/diretorio", db)
    escreve_terminal(site, "Digite 'baudrate' ou 'br' para visualizar/alterar o valor da baudrate", db)    
    escreve_terminal(site, "Digite 'ajudar'   ou 'a'  para mostrar novamente esse menu", db)
    escreve_terminal(site, "Digite 'sair'     ou 's'  para sair do script", db)
    escreve_terminal(site, "==========================================================================", db)

while(True):
    carga = False
    compila = False
    exp = ""
    projeto = ""

    escreve_terminal(termupdate, "\nDigite 'iniciar' ou 'i' para comecar a execucao do script", db)
    text = le_terminal(termget, db);

    if text == "iniciar" or text == "i":
        menu(termupdate)

        while(True):   
            text = le_terminal(termget, db);
            
            if text == "carregar" or text == "ca":
                if compila == True:
                    comando = "python carrega.py " + exp + " " + projeto 
                    os.system(comando)
                else:
                    escreve_terminal(termupdate, "Voce ainda nao compilou o projeto", db)  

            elif text == "compilar" or text == "co":
                if exp == "" or projeto == "":
                    escreve_terminal(termupdate, "Voce ainda nao colocou o nome do projeto e/ou da experiencia", db)
                else:
                    comando = "python compila.py " + exp + " " + projeto
                    if os.system(comando) != 2:
                        compila = True

            elif text == "esp8266" or text == "es":
                if carga == True:
                    escreve_terminal(termupdate, "Voce ja fez a carga do script no esp8266", db)
                else:
                    if os.system("python arduino.py") != 2:
                        carga = True

            elif text == "testar" or text == "t":
                if carga == True:
                    os.system("python testa.py")
                else:
                    escreve_terminal(termupdate, "Voce ainda nao fez a carga do script no esp8266", db)

            elif text == "pinar" or text == "pi":
                os.system("python pinagem.py")

            elif text == "exp" or text == "e":
                escreve_terminal(termupdate, "Digite o nome da experiencia (nome do arquivo .txt contendo a pinagem)", db)
                exp = le_terminal(termget, db);

                while(" " in exp or "." in exp):
                    escreve_terminal(termupdate, "Digite o nome da experiencia sem espacos nem extensao (.)", db)
                    exp = le_terminal(termget, db);       

                compila = False

            elif text == "projeto" or text == "pr":
                escreve_terminal(termupdate, "Digite o nome do projeto (nome do arquivo qar)", db)
                projeto = le_terminal(termget, db);

                while(" " in projeto or "." in projeto):
                    escreve_terminal(termupdate, "Digite o nome do projeto sem espacos nem extensao (.)", db)
                    projeto = le_terminal(termget, db);  

                compila = False
                
            elif text == "baixar" or text == "b":
                escreve_terminal(termupdate, "Digite o id do projeto no Google Drive", db)
                escreve_terminal(termupdate, "Dada uma URL por exemplo: https://drive.google.com/file/d/0B9P1L--7Wd2vU3VUVlFnbTgtS2c/view?usp=sharing", db)
                escreve_terminal(termupdate, "O id eh: 0B9P1L--7Wd2vU3VUVlFnbTgtS2c", db)
                escreve_terminal(termupdate, "Nao se esqueca que o arquivo devera estar acessivel para qualqer pessoa com o link", db)
                idd = le_terminal(termget, db);
                url = "https://drive.google.com/uc?id=" + idd
                nome = gdown.download(url)
                
                if nome == None:
                    escreve_terminal(termupdate, "Erro no download do arquivo", db)
                else:
                    escreve_terminal(termupdate, "Arquivo " + nome + " baixado com sucesso", db)

            elif text == "mostrar" or text == "m":
                escreve_terminal(termupdate, "Experiencia: " + exp, db)
                escreve_terminal(termupdate, "Projeto: " + projeto, db)

            elif text == "arquivos" or text == "ar":
                mostra_diretorio()

            elif text == "remover" or text == "r":
                escreve_terminal(termupdate, "Digite o nome do arquivo com extensao ou diretorio", db)
                arquivo = le_terminal(termget, db)
                remove_arquivo(arquivo)

            elif text == "baudrate" or text == "br":
                if os.system("python baudrate.py") == 2:
                    carga = False
                    escreve_terminal(termupdate, "Voce precisara fazer uma nova carga do script no esp8266", db)

            elif text == "ajudar" or text == "a":
                menu(termupdate)

            elif text == "sair" or text == "s":
                escreve_terminal(termupdate, "Saindo do script top", db)
                break

            else:
                escreve_terminal(termupdate, "Comando invalido. Digite 'ajudar' ou 'a' para mostrar novamente os comandos validos", db)

            if text != "ajudar" and text != "a":
                escreve_terminal(termupdate, "==========================================================================", db)
                escreve_terminal(termupdate, "Voce esta no menu do script do LabEAD", db)
                escreve_terminal(termupdate, "==========================================================================", db)

    else:
        escreve_terminal(termupdate, "Comando invalido", db)