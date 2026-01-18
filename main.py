import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


URL = "https://www.sefaz.mt.gov.br/nfce/consultanfce?p=51260124118896000176650090005334571005642263%7C2%7C1%7C1%7CC1E1D6FB1E609D03BE43399B550190AF03AC0D0A"


def buscar_pagina(url):
    response = requests.get(url)
    if response.status_code == 200:
        pagina = pagina = BeautifulSoup(response.text, "html.parser")
        print("Requisição OK!")
        return pagina
    else:
        print("URL inválida!")
        return None


def pegar_estabelecimento(pagina):
    if pagina is not None:
        elemento = pagina.find("div", class_="txtTopo")
        if elemento:
            return elemento.text
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_cnpj(pagina):
    if pagina is not None:
        elemento = pagina.find_all("div", class_="text")[0]
        if elemento:
            return elemento.text.replace("\t", "").replace("\n", "")
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_endereco(pagina):
    if pagina is not None:
        elemento = pagina.find_all("div", class_="text")[1]
        if elemento:
            return elemento.text.replace("\t", "").replace("\n", "")
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_forma_pagamento(pagina):
    if pagina is not None:
        elemento = pagina.find_all("label", class_="tx")[0]
        if elemento:
            return elemento.text.replace("\t", "").replace("\n", "")
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_num_nota(pagina):
    if pagina is not None:
        elemento = pagina.find_all("ul")[0].find("li")
        elemento = elemento.get_text(" ", strip=True)
        elemento = elemento.split()
        elemento = elemento[3]

        if elemento:
            return elemento
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_serie_nota(pagina):
    if pagina is not None:
        elemento = pagina.find_all("ul")[0].find("li")
        elemento = elemento.get_text(" ", strip=True)
        elemento = elemento.split()
        elemento = elemento[5]

        if elemento:
            return elemento
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_data_emissao(pagina):
    if pagina is not None:
        elemento = pagina.find_all("ul")[0].find("li")
        elemento = elemento.get_text(" ", strip=True)
        elemento = elemento.split()
        elemento = elemento[7]

        if elemento:
            return elemento
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_hora_emissao(pagina):
    if pagina is not None:
        elemento = pagina.find_all("ul")[0].find("li")
        elemento = elemento.get_text(" ", strip=True)
        elemento = elemento.split()
        elemento = elemento[8]

        if elemento:
            return elemento
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_protocolo(pagina):
    if pagina is not None:
        elemento = pagina.find_all("ul")[0].find("li")
        elemento = elemento.get_text(" ", strip=True)
        elemento = elemento.split()
        elemento = elemento[15]

        if elemento:
            return elemento
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_data_protocolo(pagina):
    if pagina is not None:
        elemento = pagina.find_all("ul")[0].find("li")
        elemento = elemento.get_text(" ", strip=True)
        elemento = elemento.split()
        elemento = elemento[16]

        if elemento:
            return elemento
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_hora_protocolo(pagina):
    if pagina is not None:
        elemento = pagina.find_all("ul")[0].find("li")
        elemento = elemento.get_text(" ", strip=True)
        elemento = elemento.split()
        elemento = elemento[17]

        if elemento:
            return elemento
        else:
            print("Elemento inexistente")
            return None

    else:
        print("Página vazia!")

        return None


def pegar_produtos(pagina):
    lista = []
    # dados = dict()
    if pagina is not None:
        produtos = pagina.find_all("table")[1].find_all("tr")
        for produto in produtos:
            nome_produto = produto.find("span", class_="txtTit").get_text().strip()

            cod_produto = (
                produto.find("span", class_="RCod")
                .get_text()
                .replace("\t", "")
                .replace("\n", "")
            )[8:-1].strip()

            qtd_produto = (
                produto.find("span", class_="Rqtd")
                .get_text()[6:]
                .strip()
                .replace(",", ".")
            )

            uni_produto = produto.find("span", class_="RUN").get_text()[3:].strip()

            val_unit_produto = (
                (
                    produto.find("span", class_="RvlUnit")
                    .get_text()
                    .replace("\t", "")
                    .replace("\n", "")
                )[10:]
                .strip()
                .replace(",", ".")
            )

            val_total_produto = (
                produto.find("span", class_="valor")
                .get_text()
                .strip()
                .replace(",", ".")
            )

            dados = {
                "nome": nome_produto,
                "codigo": cod_produto,
                "quantidade": float(qtd_produto),
                "unidade": uni_produto,
                "valor_unitario": float(val_unit_produto),
                "valor_total": float(val_total_produto),
            }
            lista.append(dados)

        return lista


pagina = buscar_pagina(URL)
estabelecimento = pegar_estabelecimento(pagina)
cnpj = pegar_cnpj(pagina)
endereco = pegar_endereco(pagina)
pagamento = pegar_forma_pagamento(pagina)
info_nota_numero = pegar_num_nota(pagina)
serie_nota = pegar_serie_nota(pagina)
data_emissao = pegar_data_emissao(pagina)
hora_emissao = pegar_hora_emissao(pagina)
protocolo = pegar_protocolo(pagina)
data_protocolo = pegar_data_protocolo(pagina)
hora_protocoloc = pegar_hora_protocolo(pagina)


print(f"""
===== DADOS DA NFC-e =====

Estabelecimento: {estabelecimento}
CNPJ: {cnpj}
Endereço: {endereco}

Forma de pagamento: {pagamento}

Número da Nota: {info_nota_numero}
Série: {serie_nota}
Data de Emissão: {data_emissao}
Hora de Emissão: {hora_emissao}

Protocolo: {protocolo}
Data do Protocolo: {data_protocolo}
Hora do Protocolo: {hora_protocoloc}

==========================
""")

print("Lista de compras:\n\n==========================")
# URL = "https://www.sefaz.mt.gov.br/nfce/consultanfce?p=51260109477652019610651100000027241902953355|2|1|1|37780E9EEC7023546CB9EF4EB15B5E3EE4734C32"
# pagina = buscar_pagina(URL)
dados = pegar_produtos(pagina)
df = pd.DataFrame(dados)
print(df.head(12))
# print(df.info())
