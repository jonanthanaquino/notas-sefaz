import requests
from bs4 import BeautifulSoup

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


pagina = buscar_pagina(URL)
estabelecimento = pegar_estabelecimento(pagina)

print(f"O nome do estabelecimento é: {estabelecimento}")
