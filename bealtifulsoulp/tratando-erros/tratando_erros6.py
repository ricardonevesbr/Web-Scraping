from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost:8000")
bsObj = BeautifulSoup(html.read(), "html.parser")

if bsObj.html.tag_nao_existente is not None:
    print(bsObj.html.tag_nao_existente.outra_tag)
else:
    print("bsObj.html.tag_nao_existente é None")

if bsObj.html is not None:
    resultado = bsObj.html.body
    print("bsObj.html.body ok. bsObj.html não é None.")
else:
    print("bsObj.html é None")

if bsObj.html is not None:
    resultado = bsObj.html.bodyTeste
    print(f"Resultado: {resultado}") #html não é None, mas bodyTeste é None.
else:
    print("bsObj.html é None")