from bs4 import BeautifulSoup
import requests

site = requests.get("https://climatempo.com.br/").content
# objeto site esta recebendo todo o conteúdo da requisição do site ...

soup = BeautifulSoup(site, 'html.parser')
# objeto soup esta baixando do site o html do site

# print(soup.prettify())
# transforma o html em string, o print vai exibir o codigo html

print(soup.title.string)
print(soup.p.string)
print(soup.a.string)
