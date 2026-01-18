import requests
from bs4 import BeautifulSoup
url = "https://www.sefaz.mt.gov.br/nfce/consultanfce?p=51260124118896000176650090005334571005642263%7C2%7C1%7C1%7CC1E1D6FB1E609D03BE43399B550190AF03AC0D0A"
response = requests.get(url)

print (response)

soup = BeautifulSoup(response.text, "html.parser")

print(soup)