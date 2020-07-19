from lxml import html, etree
from urllib.request import urlopen

pagina = urlopen("https://www.pythonparatodos.com.br/formulario.html")
tree = html.fromstring(pagina.read())
input = tree.xpath('//input[@name="celular"]')
print(input)
for elemento in input:
    print(etree.tostring(elemento))