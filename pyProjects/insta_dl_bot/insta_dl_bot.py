from bs4 import BeautifulSoup
import requests

url = "https://www.instagram.com/davybossin/?hl=en"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

pictures = doc.find_all(text="/p/")

print(pictures)


