from urllib.request import urlopen
html = urlopen("https://evaldowolkers.wordpress.com/")
print(html.read())

