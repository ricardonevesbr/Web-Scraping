import json

jsonString = """
{
    "arrayNumeros":[{"numero":1},{"numero":2},{"numero":3}],
    "arrayFrutas":[{"fruta":"banana"},{"fruta":"uva"},{"fruta":"maçã"}]
}
"""

jsonObjeto = json.loads(jsonString)

print(jsonObjeto.get('arrayNumeros'))
print(jsonObjeto.get('arrayFrutas'))
print(jsonObjeto.get('arrayNumeros')[2])
print(jsonObjeto.get('arrayNumeros')[1].get("numero") +
      jsonObjeto.get('arrayNumeros')[2].get("numero"))
print(jsonObjeto.get('arrayFrutas')[2].get("fruta"))