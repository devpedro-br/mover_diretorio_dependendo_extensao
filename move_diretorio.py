"""
Objetivo do projeto: Criar um script python que verifica se existem arquivos com uma extensão em específico e então mover seu diretorio até um destino qualquer

Autor: Pedro Lucas
Github: https://github.com/devpedro-br
Data de criação: 13/07/2019
Versão: Python 3.6.4
"""

import os, shutil


def verificar_dir(diretorio, extensao, destino):
    if (os.path.exists(diretorio) == True):
        for pasta, subpastas, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                extensao_arquivo = arquivo.endswith(extensao)
                if (extensao_arquivo == True):
                    result = ('Existem arquivos com a extensão {} na pasta'
                              ).format(extensao)
                    if (os.path.exists(destino) == True):
                        shutil.move(diretorio, destino)
                        print('Diretório movido com sucesso')
                        break
                    else:
                        result = 'O diretório de destino não existe'
                else:
                    result = ('Não existem arquivos com a extensão {} na pasta'
                              ).format(extensao)
        return print(result)

    else:
        print('Este diretório não existe')


diretorio = input('Qual é o diretório que você deseja verificar? ')
extensao = input('Qual é a extensão que você procura? ')
destino = input('Qual é o destino desse diretório? ')
print('')
verificar_dir(diretorio, extensao, destino)