import os
from ftplib import FTP
from getpass import getpass


def download(ip='', user='', pwd='', diretorio='', arquivo=''):
    try:
        cx = FTP(ip)
        cx.login(user, pwd)
        cx.cwd(diretorio)
        print('\n\n Arquivos no Diretorio:')
        print('----------------------------------------------------------------------')
        cx.retrlines('LIST')
        print('---------------------------------------------------------------------- \n\n')
        with open(arquivo, 'wb') as arquivo_baixado:
            print('Baixando...')
            cx.retrbinary('RETR ' + arquivo, arquivo_baixado.write, 1024)
            cx.quit()
            print('Download Concluido em:')
            print(f'{os.getcwd()}/{arquivo} \n\n')
    except Exception as error:
        print(error)


def upload(ip, user, pwd, arquivo_local, dir_upload = ''):
    try:
        cx = FTP(ip)
        cx.login(user, pwd)
        cx.cwd(dir_upload)
        print('\n\n Arquivos no Diretorio:')
        print('----------------------------------------------------------------------')
        cx.retrlines('LIST')
        print('---------------------------------------------------------------------- \n\n')
        local = open(arquivo_local, 'rb')
        print('Baixando...')
        cx.storbinary('STOR ' + arquivo_local, local, 1024)
        print('----------------------------------------------------------------------')
        cx.retrlines('LIST')
        cx.quit()
        print('Upload Concluido em:')
    except Exception as error:
        print(error)


ip = input('Endereço: ')
user = input('Usuario: ')
pwd = getpass()
diretorio = input('Diretório do arquivo: ')
arquivo_down = input('Nome do Arquivo Para Download: ')
arquivo2_up = input('Nome do Arquivo para Upload: ')

download(ip, user, pwd, diretorio, arquivo_down)
upload(ip, user, pwd, arquivo2_up,dir_upload=diretorio)

