import os
import re
import requests

url = "http://181.215.253.55/skips/vehicles/"

response = requests.get(url)

if response.status_code == 200:
    links = re.findall(r'href="(.*?\.png)"', response.text)
    
    if not os.path.exists("vehicles"):
        os.makedirs("vehicles")

    for link in links:
        image_url = url + link
        filename = link.split("/")[-1]
        with open(os.path.join("vehicles", filename), 'wb') as f:
            f.write(requests.get(image_url).content)
    print("Todas as imagens foram baixadas com sucesso!")
else:
    print("Falha ao acessar a URL:", response.status_code)