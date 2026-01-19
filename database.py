import sqlite3


def salvar_no_banco(df_dados_nota, df_produtos):
    conn = sqlite3.connect("nfce.db")

    df_dados_nota.to_sql("notas", conn, if_exists="append", index=False)
    df_produtos.to_sql("produtos", conn, if_exists="append", index=False)

    conn.close()
    print("Dados salvos com sucesso!")
