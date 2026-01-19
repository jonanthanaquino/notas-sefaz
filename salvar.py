from database import salvar_no_banco
from main import executar


URL = "https://www.sefaz.mt.gov.br/nfce/consultanfce?p=51260109477652019610651100000027241902953355|2|1|1|37780E9EEC7023546CB9EF4EB15B5E3EE4734C32"
executar(URL)

# def executar(url):
#     pagina = buscar_pagina(url)

#     dados_nota = extrair_dados_nota(pagina)
#     produtos = pegar_produtos(pagina)

#     numero = dados_nota["info_nota_numero"].iloc[0]
#     produtos["numero_nota"] = numero

#     salvar_no_banco(dados_nota, produtos)
