from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    html = urlopen("http://localhost:8000/erro")
except HTTPError as erro:
    print(f"Erro HTML: {erro}")

try:
    html = urlopen("http://www.xptoxyzabracadabra.com/")
except URLError as erro:
    print(f"Erro URL: {erro}")
