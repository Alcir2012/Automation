import paramiko
import os
import stat
import logging

# Configurando o logging
logging.basicConfig(
    filename='shellbox.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def autopostoPanamby():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'autopostostatusdopanamby'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Autoposto1090Panamby/autopostopanamby.pem'
    pastaOrigem = '/download/retorno'
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
                logging.info(f'Baixado: {arquivo} -> {local}')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo): {arquivo}')
        except Exception as e:
            logging.info(f'Erro ao processar {arquivo}: {e}')

    sftp.close()
    transport.close()


def autopostoValeMaisElaine():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'valemaiselaine'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/AutoPosto1090Ltda/valemaiselaine.pem'
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
                logging.info(f'Baixado: {arquivo} -> {local}')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo): {arquivo}')
        except Exception as e:
            logging.info(f'Erro ao processar {arquivo}: {e}')

    sftp.close()
    transport.close()


def autopostoValeMaisFabio():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'valemaisfabio'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/AutoPosto1090Ltda/valemaisfabio.pem'
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
                logging.info(f'Baixado: {arquivo} -> {local}')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)
            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo): {arquivo}')
        except Exception as e:
            logging.info(f'Erro ao processar {arquivo}: {e}')

    sftp.close()
    transport.close()


def autopostoValeMaisRodrigo():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'valemaisrodrigo'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/AutoPosto1090Ltda/valemaisrodrigo.pem'
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
                logging.info(f'Baixado: {arquivo} -> {local}')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)
            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo): {arquivo}')
        except Exception as e:
            logging.info(f'Erro ao processar {arquivo}: {e}')

    sftp.close()
    transport.close()


def autopostoValeMaisRogerio():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'valemaisrogerio'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/AutoPosto1090Ltda/valemaisrogerio.pem'
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
                logging.info(f'Baixado: {arquivo} -> {local}')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)
            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo): {arquivo}')
        except Exception as e:
            logging.info(f'Erro ao processar {arquivo}: {e}')

    sftp.close()
    transport.close()


def autopostoValeMaisSociedade():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'valemaissociedade'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/AutoPosto1090Ltda/valemaissociedade.pem'
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
                logging.info(f'Baixado: {arquivo} -> {local}')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)
            else:
                logging.info(f'⏭ Ignorado (não é .csv ou não é arquivo): {arquivo}')
        except Exception as e:
            logging.info(f'Erro ao processar {arquivo}: {e}')

    sftp.close()
    transport.close()


def transfereCatalogador():
    hostDestino = 'ftp.eextrato.com.br'
    usuarioDestino = 'monitoramento'
    senhaDestino = '@#kvZLGDvUl6XLonX1bl79YNgMwTasIvaY'
    pasta_remota_destino = '/eextrato/SHELLBOX'
    pasta_local = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'

    # Conectar ao segundo servidor SFTP com senha
    transport_destino = paramiko.Transport((hostDestino, 222))  # ou 22 se for padrão
    transport_destino.connect(username=usuarioDestino, password=senhaDestino)
    transport_destino.use_compression(True)
    sftp_destino = paramiko.SFTPClient.from_transport(transport_destino)

    # Enviar arquivos da pasta local
    for arquivo in os.listdir(pasta_local):
        if arquivo.endswith('.csv'):
            local_path = os.path.join(pasta_local, arquivo)
            remote_path = f"{pasta_remota_destino}/{arquivo}"

            sftp_destino.put(local_path, remote_path)
            logging.info(f' Enviado: {arquivo} -> {remote_path}')

    # Fechar conexão
    sftp_destino.close()
    transport_destino.close()


autopostoPanamby()
autopostoValeMaisElaine()
autopostoValeMaisFabio()
autopostoValeMaisRodrigo()
autopostoValeMaisRogerio()
autopostoValeMaisSociedade()
transfereCatalogador()