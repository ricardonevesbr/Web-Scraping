import re

texto = ("Esta é uma aula de Python. Esta aula é sobre Expressões regulares. "
        "Espero que goste desta aula.")

padrao = "Esdta"
resultado = re.search(padrao, texto)

if resultado:
    print(resultado.group())
else:
    print("Não encontrado")