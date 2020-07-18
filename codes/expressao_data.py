import re

padrao = re.compile(r"\d{2}/\d{2}/\d{4}")
texto = "Hoje é dia 26/09/2017, a data para entrega do produto era 10/09/2017, estamos com 16 dias em atraso."
print(re.findall(padrao, texto))
