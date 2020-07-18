# Importando o módulo re
import re

# Definindo o padrão usando uma expressão literal
padrao = "aula"
#padrao = "abacaxi"

# Definindo o texto
texto = "Esta é uma aula de Python. Nesta aula vamos falar sobre expressões regulares."

# Usando o search para pesquisar o texto que coincide com o padrão
resultado = re.search(padrao, texto)

# Imprime o match object
print(resultado)

# Imprime o texto encontrado
print(resultado.group())

"""
if resultado:
    print(resultado.group())
else:
    print("Nenhuma informação encontrada.")
"""