
import duckdb
import pandas as pd
import config   


con = duckdb.connect() # Cria uma conexão DuckDB

print("Versao:", duckdb.__version__)


con.execute("INSTALL excel")
con.execute("LOAD excel")

print("Módulo Excel instalado e carregado com sucesso.")

# fonte comum para todas as consultas.
# O arquivo Excel continua sendo a fonte de dados, mas agora podemos usar o DuckDB para consultar os dados de forma mais eficiente.



arquivo = config.Input.as_posix().replace("'", "''")
fonte = f"read_xlsx('{arquivo}', sheet='Vendas', header=true)"

consultas = {
    "Resumo": f"""
    SELECT
        COUNT(*) AS quantidade_registros,
        SUM(quantidade) AS unidades_vendidas,
        SUM(Valor_Total) AS faturamento,
        AVG(Valor_Total) AS ticket_medio
    FROM {fonte}
    """,

    "Top_10_Clientes": f"""
    SELECT cliente,
             SUM(Valor_Total) AS faturamento
    FROM {fonte}
    GROUP BY cliente
    ORDER BY faturamento DESC
    LIMIT 10
    """,

    "Menor_Faturamento": f"""
    SELECT cliente,
             SUM(Valor_Total) AS faturamento
    FROM {fonte}
    GROUP BY cliente
    ORDER BY faturamento ASC
    LIMIT 10
    """,

    "Produtos_Mais_Vendidos": f"""
    SELECT produto,
             SUM(quantidade) AS unidades_vendidas
    FROM {fonte}
    GROUP BY produto
    ORDER BY unidades_vendidas DESC
    LIMIT 10
    """,

    "Faturamento_Por_Mes": f"""
        SELECT
            DATE_TRUNC('month', CAST(Data AS DATE)) AS mes,
            SUM(Valor_Total) AS faturamento
        FROM {fonte}
        GROUP BY mes
        ORDER BY mes
    """,
}


# Executa cada consulta e cria uma aba no excel
with pd.ExcelWriter(config.Output, engine="openpyxl") as writer:
    for aba, consulta in consultas.items():
        df = con.execute(consulta).fetchdf()
        df.to_excel(
            writer,
            sheet_name=aba,
            index=False)

con.close()
print("Arquivo de saída gerado com sucesso:", config.Output)