import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
tabla = soup.find("div", class_="quote")
datos = []

if citas:
    filas = citas.find_all("div")[1:]

        texto = cita.find("span", class_="text").text.strip()
        autor = cita.find("small", class_="author").text.strip()
        tags = ", ".join([tag.text.strip() for tag in cita.find_all("a", class_="tag")])

        datos.append({
            "Quote": texto,
            "Autor": autor,
            "Tags": tags
            })

    df = pd.DataFrame(datos)
    df.to_csv("quotes.csv", index=False, encoding="utf-8-sig")
    print("Scraping exitoso y archivo quote.csv creado.")
else:
    print("No se encontró ninguna tabla en la página")
