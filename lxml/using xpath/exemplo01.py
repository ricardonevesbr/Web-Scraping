from lxml import html, etree
from urllib.request import urlopen

pagina = urlopen("https://www.pythonparatodos.com.br/formulario.html")
tree = html.fromstring(pagina.read())
body = tree.xpath('/html/body')
print(body)
for elemento in body:
    print(etree.tostring(elemento))