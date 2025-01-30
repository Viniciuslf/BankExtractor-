import pdfplumber
import re


def extrair_dados_extrato(pdf_path):
    dados = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            texto = page.extract_text()
            if texto:
                linhas = texto.split('\n')
                for linha in linhas:
                    if re.search(r'\d{2}/\d{2}/\d{4}', linha):  # Detecta data
                        dados.append(linha)

    return dados


# Exemplo de uso
pdf_path = "extrato.pdf"  # Substitua pelo caminho do seu arquivo
transacoes = extrair_dados_extrato(pdf_path)

for transacao in transacoes:
    print(transacao)
