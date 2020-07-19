from lxml import etree
import locale


# Carregar os dados das despesas para um dicionário
# A chave do dicionário terá o nome do deputado
def carregar_dados():
    dicionario_deputado = {} # Criando um dicionário vazio - Este dicionário vai conter vários dicionários
    tree = etree.parse("../desafio1/Ano-2017.xml") # Carregando o arquivo XML
    lista_despesas = tree.findall('DESPESAS') # Carregando uma lista de objetos DESPESAS
    for despesa in lista_despesas: # Carregando cada objeto DESPESAS
        for informacao in despesa: # Carregando cada objeto DESPESA
            propriedades = informacao.getchildren() # Carregando cada informação do objeto DESPESA
            if propriedades[18].tag == 'vlrLiquido': # Validando se o valor líquido existe no registro (alguns registros estão sem esta informação)
                nome = propriedades[0].text # Pegando o nome do deputado
                categoria = propriedades[8].text # Pegando a categoria da despesa
                valor_despesa = propriedades[18].text # Pegando o valor da despesa

                valor_despesa = float(valor_despesa.replace(',', '.'))

                if nome in dicionario_deputado: # Se já existe uma chave com o nome do deputado no dicionário
                    dicionario = dicionario_deputado[nome] # Carrega os dados do dicionario_deputado (que também são dicionários) cuja chave seja o nome do deputado
                    if categoria in dicionario: # se 'dicionario' possuir uma chave com a categoria da despesa
                        dicionario[categoria] += valor_despesa # Soma a despesa ao valor existente
                    else: # Caso contrário
                        dicionario[categoria] = valor_despesa # Adiciona a chave com nome da categoria e valor da despesa

                    dicionario_deputado[nome] = dicionario # Adicionado o novo dicionário à dicionario_deputado cuja chave seja o nome do deputado
                else: # Se não existe o dicionário com o nome do deputado como chave
                    dic = {} # Cria um dicionário vazio
                    dic[categoria] = valor_despesa # Adiciona o valor da despesa usando como chave o nome da categoria
                    dicionario_deputado[nome] = dic # Adiciona o novo dicionário no dicionário de deputados, tendo como chave, o nome do deputado

    return dicionario_deputado # Retorna o dicionário de deputados

def formatar_valor(valor):
    if "," not in valor:
        valor_despesa = valor + ",00"

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')  # MUDAR A CONFIGURAÇÃO DE MOEDA, NÚMEROS, ETC PARA pt_BR
    valor = locale.currency(valor, grouping=True, symbol=None)  # FORMATAR A VARIÁVEL valor COMO MOEDA, SEM SÍMBOLO (R$) E COLOCANDO O PONTO PARA MILHAR
    locale.setlocale(locale.LC_ALL, '')  # RETORNANDO A CONFIGURAÇÃO PADRÃO DO SISTEMA
    return valor

if __name__ == "__main__":
    dicionario = carregar_dados()
    print(dicionario)

    while True:
        total_despesas = 0
        deputado = input("Informe o nome do deputado (ou 0 (zero) para sair): ").upper()
        if deputado == "0":
            break
        elif deputado in dicionario:
            for chave, valor in dicionario[deputado].items():
                total_despesas += valor
                valor = formatar_valor(valor)
                print(f'{chave}: {valor}')
        else:
            input("Deputado não localizado! Pressione qualquer tecla ver a lista de deputados.")
            for nome in dicionario.keys():
                print(nome)

        total_despesas = formatar_valor(total_despesas)
        print(f"Total Despesas: {total_despesas}")

    print("---Obrigado por utilizar o sistema---")
