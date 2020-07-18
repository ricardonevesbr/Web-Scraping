import requests
import bs4

response = requests.get("https://evaldowolkers.wordpress.com/")
soup = bs4.BeautifulSoup(response.text, "html.parser")

print(soup.find_all('title'))
