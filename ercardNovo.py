from ftplib import FTP
import os
import logging
import paramiko

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Caminho absoluto para o log
log_path = os.path.join(script_dir, 'ercard.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def baixaErcard():
    host = 'ftp.flavios.com.br'
    user = 'ercard'
    senha = 'bgt5CDE#mju7'
    pastaOrigem = '/'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    pastaProcessados = '/Processado'
    
    os.makedirs(pastaLocal, exist_ok= True)
    
    try:
        ftp = FTP()
        ftp.connect(host,21)
        ftp.login(user,senha)
        ftp.cwd(pastaOrigem)
        arquivos = ftp.nlst()

        for arquivo in arquivos:
            if arquivo.endswith('.TXT'):
                local_path = os.path.join(pastaLocal,arquivo)
                with open(local_path,'wb') as f:
                    ftp.retrbinary(f'RETR {arquivo}', f.write)
                logging.info(f'Baixando: {arquivo} para -> Pasta local')
                try:
                    ftp.rename(arquivo,f'{pastaProcessados}/{arquivo}')
                except Exception as e:
                    logging.warning(f'Erro ao tentar mover {arquivo} para {pastaProcessados} devido a {e}')
            else:
                logging.info(f'Ignorado oque não for txt')

        ftp.quit()
    except Exception as e:
        logging.error(f'Erro geral {e}')
 

def transfereCatalogador():
    hostDestino = 'ftp.eextrato.com.br'
    usuarioDestino = 'monitoramento'
    senhaDestino = '@#kvZLGDvUl6XLonX1bl79YNgMwTasIvaY'
    pasta_remota_destino = '/eextrato/ERCARD/'
    pasta_staging = '/eextrato/ERCARD/TRATADOS'
    pasta_local = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'

    # Conectar ao segundo servidor SFTP com senha
    transport_destino = paramiko.Transport((hostDestino, 222))  # ou 22 se for padrão
    transport_destino.connect(username=usuarioDestino, password=senhaDestino)
    transport_destino.use_compression(True)
    sftp_destino = paramiko.SFTPClient.from_transport(transport_destino)

    # Enviar arquivos da pasta local
    for arquivo in os.listdir(pasta_local):
        if arquivo.startswith('335'):
            local_path = os.path.join(pasta_local, arquivo)
            staging_path = f"{pasta_staging}/{arquivo}"
            remote_path = f"{pasta_remota_destino}/{arquivo}"

            sftp_destino.put(local_path, staging_path)
            logging.info(f' Enviado: {arquivo} para -> SFTP BoaVista')

            sftp_destino.rename(staging_path,remote_path)
            logging.info(f'{arquivo} enviado para -> catalogador')

            os.remove(local_path)
            logging.info('Removido localmente')

    # Fechar conexão
    sftp_destino.close()
    transport_destino.close()

baixaErcard()
transfereCatalogador()