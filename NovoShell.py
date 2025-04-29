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

def posto_bauer():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'bauerpostoscomdecombeconvltd-2'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Bauer Postos e Comercio/postobauer.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def cafeda_terra():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'cafedaterra-40939392000173'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/cafedaterra-40939392000173.com.br.ppk/cafedaterra.pem'
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

def falcao():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'falcao-10588194000141'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/falcao-10588194000141.com.br/falcao.pem'
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

def jmi_comercio():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'toscano-05932284000259'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/JMI comercio de derivados de petroleo/jmi.pem'
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

def manaus():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'manauscomdederivdepetroleoltd'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/manauscomdederivdepetroleoltd.com.br (2)/manaus.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def parebem_posto():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'redepdfpostoesplanada-35915682'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/PAREBEMPOSTOSANTO/parebemposto.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()


def tamboril():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'rionegrocomderivdepetro'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Petroleo Tamboril/tamboril.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def planalto_petroleo():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'planaltopetroleoceasaltda'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/POSTOSR4/planaltopetroleo.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def santa_amelia():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'liber-33899485000156'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto de Abastecimento a Gas Santa Amelia/santaamelia.pem'
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

def lajuma_posto():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'enzoitaipava-1904245000106'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto de Combustíveia Comercial Lajuma/lajuma.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_paz():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'portalestreladomorumbictroaut-'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto de Serviços Paz/postopaz.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_palhaseca():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'postopalhaseca'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto Palha Verde/postopalhaseca.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_phoenix():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'phoenixrededepostos'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto Phoenix/postophoenix.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_rfd():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'autopostolopescachamorra'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto RFDKM/postorfd.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_rfd_km():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'km-33643875000160'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto RFDKM/postorfd_km.pem'
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

def posto_loyola():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'postopeliberio'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto Santo Inacio De Loyola/postoloyola.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_mogi():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'postoqualitycasablanca'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto Shopping Mogi/mogi.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_kailandia():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'postokalilandia'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Rede kailandia/kailandia.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_universo():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'autopostouniverso'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Auto Posto Universo/postouniverso.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_boavista():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'postoboavista'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Postos Setee/postoboavista.pem'
    pastaOrigem = '/download'
    pastaLocal = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'
    pastaProcessados = '/download/Processados'

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

def posto_dompedro():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'rededompedrodepostos-204152950'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Rede dom Pedro de Postos/dompedro.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def posto_esplanada():
    host = 'ftp02.main.sao.equals.com.br'
    usuario = 'redepdfpostoesplanada-35915682'
    caminhoChave = 'C:/Certificados Operadoras/Shellbox/Posto esplanada/postoesplanada.pem'
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
                logging.info(f'Baixado: {arquivo} -> Pasta local')
                caminhoProcesados = f"{pastaProcessados}/{arquivo}"
                sftp.rename(caminho_remoto, caminhoProcesados)

            else:
                logging.info(f'⏭️ Ignorado (não é .csv ou não é arquivo)')
        except Exception as e:
            logging.info(f'Erro ao baixar para pasta local {arquivo}: {e}')

    sftp.close()
    transport.close()

def transfereCatalogador():
    hostDestino = 'ftp.eextrato.com.br'
    usuarioDestino = 'monitoramento'
    senhaDestino = '@#kvZLGDvUl6XLonX1bl79YNgMwTasIvaY'
    pasta_staging = '/eextrato/SHELLBOX/TRATADOS'
    pasta_remota_destino = '/eextrato/SHELLBOX'
    pasta_local = 'C:/Users/jose.alcir/Documents/ArquivosDiarios'

    # Conectar ao segundo servidor SFTP com senha
    transport_destino = paramiko.Transport((hostDestino, 222))  # ou 22 se for padrão
    transport_destino.connect(username=usuarioDestino, password=senhaDestino)
    transport_destino.use_compression(True)
    sftp_destino = paramiko.SFTPClient.from_transport(transport_destino)

    transport_destino.window_size = 3 * 1024 * 1024  # 3 MB
    channel = transport_destino.open_session()
    channel.settimeout(30)

    # Enviar arquivos da pasta local
    for arquivo in os.listdir(pasta_local):
        if arquivo.endswith('.csv'):
            local_path = os.path.join(pasta_local, arquivo)
            staging_path = f"{pasta_staging}/{arquivo}"
            remote_path = f"{pasta_remota_destino}/{arquivo}"

            sftp_destino.put(local_path, staging_path)
            logging.info(f' Enviado para processamento: {arquivo} -> "SFTP BoaVista"')

            sftp_destino.rename(staging_path,remote_path)
            logging.info(f'Tirando arquivo {arquivo} para -> Catalogador')

            os.remove(local_path)
            logging.info(f'Removido localmente: {arquivo}')

    # Fechar conexão
    sftp_destino.close()
    transport_destino.close()

anf_combustiveis()
autoposto_totality()
autoposto_tupy()
autoposto_pontal()
posto_bauer()
cafeda_terra()
falcao()
jmi_comercio()
manaus()
parebem_posto()
tamboril()
planalto_petroleo()
santa_amelia()
lajuma_posto()
posto_paz()
posto_palhaseca()
posto_phoenix()
posto_rfd()
posto_rfd_km()
posto_loyola()
posto_mogi()
posto_kailandia()
posto_universo()
posto_boavista()
posto_dompedro()
posto_esplanada()
transfereCatalogador()