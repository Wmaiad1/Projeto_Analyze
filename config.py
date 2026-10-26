from pathlib import Path

# Caminhos do Projeto pastas

Arquivos = Path(__file__).resolve().parent # diretório do arquivo config.py
Input = Arquivos / "planilha.xlsx" # caminho do arquivo de entrada
Output = Arquivos.parent / "relatório.xlsx" # caminho do arquivo de saída
