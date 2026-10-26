from pathlib import Path


# Caminhos do Projeto pastas

projeto_analyze = Path(__file__).resolve().parent # diretório do arquivo config.py
Input = projeto_analyze / "Arquivos" / "planilha.xlsx" # caminho do arquivo de entrada
Output = projeto_analyze / "Arquivos" / "relatório.xlsx" # caminho do arquivo de saída


