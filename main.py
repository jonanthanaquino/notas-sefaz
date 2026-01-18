import requests
from bs4 import BeautifulSoup
import re

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

        # data_autorizacao = elemento[16]
        # hora_autorizacao = elemento[17]


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
