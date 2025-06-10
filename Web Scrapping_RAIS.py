### --- Extração de dados da RAIS através da plataforma Base dos Dados utilizando web scrapping ---

# --- 1. INSTALANDO E IMPORTANDO BIBLIOTECAS NECESSÁRIAS
## Bibliotecas necessárias a serem instaladas
!pip install basedosdados pandas
!pip install openpyxl

## Importando bibliotecas necessárias
import pandas as pd                             
import basedosdados as bd

# --- 2. CONFIGURAÇÃO DOS PARÂMETROS ---
# Definindo  os parâmetros da consulta.
anos = [2015, 2019]
id_municipio_vca = '2933307' # Código IBGE para Vitória da Conquista

# --- 3. MONTAGEM DA CONSULTA SQL ---
# A consulta SQL foi ajustada aplicando os seguintes filtros:
# - Anos: 2015 e 2019
# - Município: Vitória da Conquista (2933307)
# - Vínculo: CLT U/PJ IND (código '10')
# - Carga Horária: 41 a 44 horas semanais (código '6')

query = f"""
SELECT
    ano,
    id_municipio,
    tipo_vinculo,
    faixa_horas_contratadas,
    quantidade_horas_contratadas,
    cbo_2002,
    grau_instrucao_apos_2005,
    subsetor_ibge,
    valor_remuneracao_media
FROM
    `basedosdados.br_me_rais.microdados_vinculos`
WHERE
    ano IN ({', '.join(map(str, anos))})
    AND id_municipio = '{id_municipio_vca}'
    AND tipo_vinculo = '10'
    AND faixa_horas_contratadas = '6'
"""

# --- 4. EXECUÇÃO DA CONSULTA E DOWNLOAD DOS DADOS ---
# Adicionando o 'billing_project_id' 
billing_project_id = "basedosdados-381718" 

print("Iniciando o download dos dados da Base dos Dados...")
print("Isso pode levar alguns minutos...")

# EXECUTANDO A CONSULTA
try:
    # A biblioteca pedirá autenticação na primeira vez que for executada.
    df = bd.read_sql(query, billing_project_id=billing_project_id)
    print("\nDownload concluído com sucesso!")

    # --- 5. SEPARAÇÃO E SALVAMENTO DOS ARQUIVOS ---
    # Separando os dados por ano e salvando em arquivos .xlsx

    # Separando o DataFrame de 2015
    df_2015 = df[df['ano'] == 2015]
    arquivo_2015 = 'rais_vca_2015.xlsx'
    df_2015.to_excel(arquivo_2015, index=False)
    print(f"Dados de 2015 salvos em: {arquivo_2015}")

    # Separando o DataFrame de 2019
    df_2019 = df[df['ano'] == 2019]
    arquivo_2019 = 'rais_vca_2019.xlsx'
    df_2019.to_excel(arquivo_2019, index=False)
    print(f"Dados de 2019 salvos em: {arquivo_2019}")
    
    print("\nProcesso finalizado!")

except Exception as e:
    print(f"\nOcorreu um erro: {e}")
    print("\nVerifique se você está logado na conta Google correta e se o projeto 'basedosdados-381718' tem o BigQuery API ativado.")
    print("Para autenticar novamente, você pode precisar apagar a pasta de credenciais da basedosdados no seu computador.")