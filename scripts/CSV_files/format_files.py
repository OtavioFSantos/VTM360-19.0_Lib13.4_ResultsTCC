
import os
import pandas as pd

def formatar_numero(numero):
    # Remove pontos
    numero_sem_ponto = numero.replace('.', '')
    
    # Move o ponto para a posição correta
    if len(numero_sem_ponto) > 3:
        numero_sem_ponto = numero_sem_ponto[:-3] + '.' + numero_sem_ponto[-3:]
    
    return float(numero_sem_ponto)

def converter_csv(diretorio_origem, diretorio_destino):
    # Lista todos os arquivos no diretório de origem
    arquivos = [arquivo for arquivo in os.listdir(diretorio_origem) if arquivo.endswith(".csv")]

    # Loop através de cada arquivo CSV
    for arquivo in arquivos:
        caminho_arquivo_origem = os.path.join(diretorio_origem, arquivo)

        # Lê o arquivo CSV
        df = pd.read_csv(caminho_arquivo_origem)

        # Converte 'Bitrate' para string, aplica a formatação e converte de volta para float
        df['Bitrate'] = df['Bitrate'].astype(str).apply(formatar_numero)

        # Define o caminho do arquivo de destino
        caminho_arquivo_destino = os.path.join(diretorio_destino, arquivo)

        # Salva o arquivo CSV convertido no diretório de destino
        df.to_csv(caminho_arquivo_destino, index=False)

if __name__ == "__main__":
    # Substitua 'caminho_do_diretorio_origem' pelo caminho do diretório onde estão os arquivos CSV originais
    caminho_do_diretorio_origem = 'C:/Users/otavi/OneDrive/Ambiente de Trabalho/TCC/VTM360-19.0_Lib13.4_ResultsTCC/CSV_files'

    # Substitua 'caminho_do_diretorio_destino' pelo caminho do diretório onde deseja salvar os arquivos convertidos
    caminho_do_diretorio_destino = 'C:/Users/otavi/OneDrive/Ambiente de Trabalho/TCC/VTM360-19.0_Lib13.4_ResultsTCC/CSV_files/updated'

    converter_csv(caminho_do_diretorio_origem, caminho_do_diretorio_destino)
