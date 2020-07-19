from lxml import etree

clientes = etree.Element("clientes")

cliente1 = etree.SubElement(clientes, "cliente1")
nome1 = etree.SubElement(cliente1, "nome")
nome1.text = "Fulano de Marte"

cliente2 = etree.Element("cliente2")
nome2 = etree.SubElement(cliente2, "nome")
nome2.text = "Anabelle de Saturno"
clientes.append(cliente2)

cliente3 = etree.Element("cliente3")
nome3 = etree.SubElement(cliente3, "nome")
nome3.text = "Plutonilda"
clientes.append(cliente3)

# len(Element) retorna a quantidade de tags do objeto
print("Total de clientes:", len(clientes))

# Criando um objeto com base no segundo elemento
cliente_dois = clientes[1]
# Imprimindo a tag do elemento de índice 1, que é
print("Tag clientes[1]:", cliente_dois.tag)

# Percorrento o Element como uma lista
for x in clientes:
    print(x.tag)

print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))

# Inserindo um elemento usando insert
clientes.insert(0, etree.Element("cliente0"))
print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))

# Fatiando a lista clientes, pegando os elementos de 1 a 2
# porque [1:3] não inclui o 3
fatia1 = clientes[1:3]
for x in fatia1:
    print(x.tag)

print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))
# O elemento da posição 2 (cliente2) vai ser substituído
# pelo elemento da posição 1 cliente1, ficando apenas os
# elementos 0, 1 e 3
clientes[2] = clientes[1]
print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))

# Verifica se clientes é 'pai' de clientes[1]
print(clientes is clientes[1].getparent())