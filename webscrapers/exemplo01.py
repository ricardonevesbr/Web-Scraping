import re
from urllib.request import urlopen


html = urlopen("http://www.pythonparatodos.com.br/contato")
texto = html.read()

padrao = r'[\w.-]+@[\w.-]+'
resultado = re.findall(padrao, str(texto))
print(resultado)

padrao = r'\(\d{2}\) \d{5}\-\d{4}'
resultado = re.findall(padrao, str(texto))
print(resultado)

