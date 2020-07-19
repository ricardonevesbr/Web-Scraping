from lxml import etree

# Como elementos XML aceitam atributos
# Você pode adicionar atributos como dicionários chave=valor
clientes = etree.Element("clientes", atributo = "valor")
cliente1 = etree.SubElement(clientes, "cliente1")
nome1 = etree.SubElement(cliente1, "nome")
nome1.text = "Fulano de Tal"

print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))


# Adicionando um atributo denominado código com valor 1248
clientes.set("codigo", "1248")
print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))
# Imprimindo o valor do atributo código
print(clientes.get("codigo"))

# Imprimindo os atributos de clientes (Element)
print(clientes.keys())

for atributo, valor in sorted(clientes.items()):
    print(f"{atributo} = {valor}")

# Pegando os atributos
atributos = clientes.attrib

print(atributos["codigo"])
print(atributos.get("atributo-inexistente"))

atributos["atributo"] = "Valor do atributo"
print(atributos["atributo"])
print(clientes.get("atributo"))

# Atributos podem ser copiados para dicionários
d = dict(clientes.attrib)
print(sorted(d.items()))