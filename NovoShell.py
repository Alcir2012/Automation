import paramiko
import os
import stat
import logging

# Configurando o logging
logging.basicConfig(
    filename='shellboxNovo.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def anf_combustiveis():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'girleno-30757976000174'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Anf Combustiveis E Comercio Eireli/anfcombustiveis.pem'
    pastaOrigem = '/download/retorno/layout-equals'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    pastaProcessados = '/download/retorno/layout-equals/Processados'

    os.makedirs(pastaLocal, exist_ok=True)

    chavePrivada = paramiko.RSAKey.from_private_key_file(caminhoChave)

    transport = paramiko.Transport((host, 20220))
    transport.connect(username=usuario, pkey=chavePrivada)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.chdir(pastaOrigem)
    arquivos = sftp.listdir()

    for arquivo in arquivos:
        caminho_remoto = f"{pastaOrigem}/{arquivo}"
        
        try:
            info = sftp.stat(caminho_remoto)
            # Verifica se é arquivo regular (não é pasta)
            if stat.S_ISREG(info.st_mode) and arquivo.endswith('.csv'):
                local = os.path.join(pastaLocal, arquivo)
                sftp.get(arquivo, local)
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def autoposto_totality():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'postoqualityfiorano'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Auto Posto Totality/autopostotality.pem'
    pastaOrigem = '/download/retorno/'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    pastaProcessados = '/download/retorno/Processados'

    os.makedirs(pastaLocal, exist_ok=True)

    chavePrivada = paramiko.RSAKey.from_private_key_file(caminhoChave)

    transport = paramiko.Transport((host, 20220))
    transport.connect(username=usuario, pkey=chavePrivada)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.chdir(pastaOrigem)
    arquivos = sftp.listdir()

    for arquivo in arquivos:
        caminho_remoto = f"{pastaOrigem}/{arquivo}"
        
        try:
            info = sftp.stat(caminho_remoto)
            # Verifica se é arquivo regular (não é pasta)
            if stat.S_ISREG(info.st_mode) and arquivo.endswith('.csv'):
                local = os.path.join(pastaLocal, arquivo)
                sftp.get(arquivo, local)
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()


def autoposto_tupy():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'postodanave-28280414000130'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Auto Posto Tupy/autopostotupy.pem'
    pastaOrigem = '/download/retorno/'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    pastaProcessados = '/download/retorno/Processados'

    os.makedirs(pastaLocal, exist_ok=True)

    chavePrivada = paramiko.RSAKey.from_private_key_file(caminhoChave)

    transport = paramiko.Transport((host, 20220))
    transport.connect(username=usuario, pkey=chavePrivada)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.chdir(pastaOrigem)
    arquivos = sftp.listdir()

    for arquivo in arquivos:
        caminho_remoto = f"{pastaOrigem}/{arquivo}"
        
        try:
            info = sftp.stat(caminho_remoto)
            # Verifica se é arquivo regular (não é pasta)
            if stat.S_ISREG(info.st_mode) and arquivo.endswith('.csv'):
                local = os.path.join(pastaLocal, arquivo)
                sftp.get(arquivo, local)
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def autoposto_pontal():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'autopostopontaldacruz-61046190'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/autopostopontaldacruz-61046190.com.br/autopostopontal.pem'
    pastaOrigem = '/download/retorno/'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    pastaProcessados = '/download/retorno/Processados'

    os.makedirs(pastaLocal, exist_ok=True)

    chavePrivada = paramiko.RSAKey.from_private_key_file(caminhoChave)

    transport = paramiko.Transport((host, 20220))
    transport.connect(username=usuario, pkey=chavePrivada)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.chdir(pastaOrigem)
    arquivos = sftp.listdir()

    for arquivo in arquivos:
        caminho_remoto = f"{pastaOrigem}/{arquivo}"
        
        try:
            info = sftp.stat(caminho_remoto)
            # Verifica se é arquivo regular (não é pasta)
            if stat.S_ISREG(info.st_mode) and arquivo.endswith('.csv'):
                local = os.path.join(pastaLocal, arquivo)
                sftp.get(arquivo, local)
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()


anf_combustiveis()
autoposto_totality()
autoposto_tupy()
autoposto_pontal()