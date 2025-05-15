#Configuração do servidor
import logging.config
import pysftp
import logging
import os
import stat
import time
from dotenv import load_dotenv

load_dotenv()

host = 'integracao.embratec.com.br'
usuario = os.getenv("goodcard_user")
senha = os.getenv("goodcard_pass")

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Caminho absoluto para o log
log_path = os.path.join(script_dir, 'goodcard.log')

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  # Ignora verificação de chave (não recomendado em produção)

try:
    with pysftp.Connection(host, username=usuario, password=senha, cnopts=cnopts) as sftp:
        sftp.cwd('/cacique')
        arquivosDisponiveis = sftp.listdir()
        logging.info(arquivosDisponiveis)
        pastaOrigem = '/cacique'
        pastaDestino ='C:/Users/jose.alcir/Documents/ArquivosDiarios'
        pastaProcessados ='/cacique/Processados'
        arquivosDuplicados = '/cacique/Novo envio (Nomenclatura duplicada)'
        if not os.path.exists(pastaDestino):
            logging.info('Pasta local não existe')

        for arquivo in arquivosDisponiveis:
            caminho_remoto = f"{pastaOrigem}/{arquivo}"

            try:
                info = sftp.stat(caminho_remoto)
            # Verifica se é arquivo regular (não é pasta)
                if stat.S_ISREG(info.st_mode) and arquivo.upper().endswith('.TXT'):
                    origem =f'/cacique/{arquivo}'
                    destino =f'C:/Users/jose.alcir/Documents/ArquivosDiarios/{arquivo}'
                    sftp.get(origem,destino)
                    time.sleep(0.5)
                    logging.info(f'Baixado: {arquivo} -> Pasta local')

                    caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                    
                    sftp.rename(caminho_remoto, caminhoProcesados)
                    logging.info(f'Movendo {arquivo} para backup')

                else:
                    logging.info(f'Ignorado (não é .txt ou não é arquivo): {arquivo}')

            except Exception as e:
                if "Failure" in str(e):
                    logging.info(f' Erro ao mover arquivo {arquivo}: {e}')
                    caminhoDuplicado = f"{arquivosDuplicados}/{arquivo}"
                    try:
                        sftp.rename(caminho_remoto,caminhoDuplicado)
                        logging.info(f"{arquivo} é duplicado, movido para pasta de duplicados")
                    except Exception as err2:
                        logging.error(f"Erro ao mover {arquivo} para pasta duplicado: {err2}")

except Exception as e:
    logging.info(f"Não foi possivel conectar: {e}")

def transfereCatalogador():
    
    hostDestino = 'ftp.eextrato.com.br'
    usuarioDestino = os.getenv("catalogador_user")
    senhaDestino = os.getenv("catalogador_pass")
    pastadeEspera = '/eextrato/GOODCARD/TRATADOS'
    pastaRemotaDestino = '/eextrato/GOODCARD/'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  

    logging.basicConfig(
    filename='uploadGoodcard.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

    try:
        with pysftp.Connection(host=hostDestino,username=usuarioDestino,password=senhaDestino, cnopts= cnopts) as sftp:
            for arquivo in os.listdir(pastaLocal):
                if arquivo.upper().endswith('.TXT'):
                    localPath = os.path.join(pastaLocal,arquivo)
                    stagingPath = f'{pastadeEspera}/{arquivo}'
                    remotePath = f'{pastaRemotaDestino}/{arquivo}'
                    sftp.put(localPath, stagingPath)
                    logging.info(f'Enviado para processamento: {arquivo} -> SFTP BoaVista')
                    sftp.rename(stagingPath,remotePath)
                    logging.info(f'Retirado da pasta de espera e inserido para catalogar')
                    os.remove(localPath)
                    logging.info(f'Removido localmente: {arquivo}')

    except Exception as e:
        logging.error(f'Erro ao transferir arquivos: {e}')

transfereCatalogador()