from urllib.request import urlopen
from urllib.error import HTTPError

html = urlopen("http://localhost:8000")
print(f"Html 1: {html}")

try:
    html = urlopen("http://localhost:8000/erro")
    print(f"Html 2: {html}")
except HTTPError as erro:
    print(erro)

html = urlopen("http://localhost:8000")
print(f"Html 3: {html}")
