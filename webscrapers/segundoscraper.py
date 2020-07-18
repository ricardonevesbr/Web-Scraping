import requests
pagina = requests.get("https://evaldowolkers.wordpress.com/")
print(pagina.text)
#print(pagina.content)
