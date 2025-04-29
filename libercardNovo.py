import paramiko
import os
import logging
import stat

#criando log
logging.basicConfig(
    filename='libercard.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

#inicio de conexão

def downloadLibercard():
    host = '150.230.92.55'
    user = 'boavistatec'
    caminhoChave = 'C:/Certificados Operadoras/Libercard/libercard.pem'
    pastaOrigem = '/extrato_libercard/'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    pastaProcessados = '/extrato_libercard/Processados/'

    os.makedirs(pastaLocal, exist_ok=True)

    chavePrivada = paramiko.RSAKey.from_private_key_file(caminhoChave)

    transport = paramiko.Transport((host,10422))
    transport.connect(username=user, pkey=chavePrivada)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.chdir(pastaOrigem)
    arquivos = sftp.listdir()

    for arquivo in arquivos:
        caminhoRemoto = f"{pastaOrigem}/{arquivo}"

        try:
            info = sftp.stat(caminhoRemoto)
            if stat.S_ISREG(info.st_mode) and arquivo.endswith('.txt'):
                local = os.path.join(pastaLocal,arquivo)
                sftp.get(arquivo,local)
                logging.info(f'Baixado: {arquivo} para -> pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminhoRemoto, caminhoProcesados)
                logging.info(f'Movendo {arquivo} para backup')
            else:
                logging.info(f'Ignorado (não é .txt ou não é arquivo): {arquivo}')
        except Exception as e:
            logging.info(f'Erro ao processar {arquivo}: {e}')

    sftp.close()
    transport.close()

def transfereAuttarCatalogador():
    hostDestino = 'ftp.eextrato.com.br'
    usuarioDestino = 'monitoramento'
    senhaDestino = '@#kvZLGDvUl6XLonX1bl79YNgMwTasIvaY'
    pastaEspera = 'eextrato/LIBERCARD/TRATADOS'
    pastaRemotaDestino= '/eextrato/LIBERCARD'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'

    transport_destino = paramiko.Transport((hostDestino, 222))  # ou 22 se for padrão
    transport_destino.connect(username=usuarioDestino, password=senhaDestino)
    transport_destino.use_compression(True)
    sftp_destino = paramiko.SFTPClient.from_transport(transport_destino)

    for arquivo in os.listdir(pastaLocal):
        if arquivo[0].isdigit():
            localPath = os.path.join(pastaLocal, arquivo)
            stagingPath = f"{pastaEspera}/{arquivo}"
            remotePath = f"{pastaRemotaDestino}/{arquivo}"

            sftp_destino.put(localPath, stagingPath)
            logging.info(f' Enviado: {arquivo} -> SFTP BoaVista')

            sftp_destino.rename(stagingPath,remotePath)
            logging.info(f'retirado {arquivo} da pasta de espera e inserido para catalogar')
            
            os.remove(localPath)
            logging.info(f'Removido localmente: {arquivo}')
    
    sftp_destino.close()
    transport_destino.close()

def transfereSoftCatalogador():
    hostDestino = 'ftp.eextrato.com.br'
    usuarioDestino = 'monitoramento'
    senhaDestino = '@#kvZLGDvUl6XLonX1bl79YNgMwTasIvaY'
    pastaRemotaDestino= '/eextrato/LIBERCARD_SOFTEXPRESS'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'

    transport_destino = paramiko.Transport((hostDestino, 222))  # ou 22 se for padrão
    transport_destino.connect(username=usuarioDestino, password=senhaDestino)
    transport_destino.use_compression(True)
    sftp_destino = paramiko.SFTPClient.from_transport(transport_destino)

    for arquivo in os.listdir(pastaLocal):
        if arquivo.startswith('LIBERCARD'):
            localPath = os.path.join(pastaLocal, arquivo)
            remotePath = f"{pastaRemotaDestino}/{arquivo}"

            sftp_destino.put(localPath, remotePath)
            logging.info(f' Enviado: {arquivo} -> SFTP BoaVista')

            os.remove(localPath)
            logging.info(f'Removido localmente: {arquivo}')

downloadLibercard()
transfereAuttarCatalogador()
transfereSoftCatalogador()