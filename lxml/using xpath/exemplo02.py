from lxml import html, etree
from urllib.request import urlopen

pagina = urlopen("https://www.pythonparatodos.com.br/formulario.html")
tree = html.fromstring(pagina.read())
table = tree.xpath('/html/body/form/table')
print(table)
for elemento in table:
    print(etree.tostring(elemento))