from lxml import etree

# funcionários será do tipo ElementTree com vários elementos
funcionarios = etree.parse(open('/home/ricardo/repos/Web-Scraping/lxml/pt2/funcionarios.xml'))

# Localizando a primeira ocorrência da tag funcionario
print(funcionarios.find("funcionario"))
# Localizando a primeira ocorrência da tag funcionario
print(funcionarios.getroot().find('funcionario'))
# Localizando todas ocorrências da tag funcionario
print(funcionarios.findall("funcionario"))

# Imprimindo o documento XML com getroot
print(etree.tostring(funcionarios.getroot(), pretty_print=True).decode("utf-8"))

# Copiando os Elements existentes no ElementTree
todos_funcionarios = funcionarios.findall("funcionario")

# Imprimindo quantos Elements encontrados
#print(len(todos_funcionarios))

for funcionario in todos_funcionarios:
    print("==========================")
    print("Tag:", funcionario.tag.strip())
    print("Text:", funcionario.text.strip())
    print("Tail:", funcionario.tail.strip())
    print("Attrib:", funcionario.attrib)

    for informacao in funcionario:
        print("**************************")
        print("Tag:", informacao.tag.strip())
        print("Text:", informacao.text.strip())
        print("Tail:", informacao.tail.strip())
        print("Attrib:", informacao.attrib)
        print("**************************")
    print("==========================")
"""
    Tag: Nome da Tag
    Text: Texto da Tag
    Tail: Texto após a Tag
    Attrib: Atributos
"""
