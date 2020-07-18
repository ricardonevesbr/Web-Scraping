import re

# Definindo o padrão usando ponto
# "." = Qualquer caracter exceto quebra de linha "\n".
# Se usar a flag DOTALL, inclui quebra de linha.
padrao = "."
texto = "\nEsta é uma aula de Python.\n Nesta aula vamos falar sobre expressões regulares.\n Espero que goste.\n"

# Sem DOTALL, ignorando \n
resultado = re.search(padrao, texto)
# Retorna a primeira ocorrência de qualquer caractere que não seja \n
print(f"*{resultado.group()}*")
#Resultado:
# *E*