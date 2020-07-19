from lxml import html, etree
from urllib.request import urlopen

pagina = urlopen("https://www.pythonparatodos.com.br/formulario.html")
tree = html.fromstring(pagina.read())
td = tree.xpath('//tr[2]/td[2]')
print(td)
for elemento in td:
    print(etree.tostring(elemento))