# comentaire sur ligne et pour un bloc il faut ... text  ...
from  key import *
import io # gestion des formats pour les fichiers json
import requests 
url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+ str(apiKey)
req = requests.get(url)
res = req.json()

articles = res.get("articles")
fichier = io.open("data.txt", "w", encoding="utf-8")

for article in articles:
    print("+++++++++++++++++++++")
    print(article["title"])
    print(article["source"] ["name"])
    
    fichier.write("+++++++++++\n")
    fichier.write(str(article["title"]) + "\n")
    
fichier.close()    