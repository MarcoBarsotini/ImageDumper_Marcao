import os, re, requests
from urllib.parse import unquote

url = input("Insira a URL que deseja clonar: ")
folder_name = input("Digite o nome da pasta que quer criar: ")
print("Certo, criando diretório chamado:", folder_name)

response = requests.get(url)

if response.status_code == 200:
    links = re.findall(r'href="(.*?\.png)"', response.text)
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for link in links:
        image_url = url + link
        filename = unquote(link).split("/")[-1] 
        filepath = os.path.join(folder_name, filename)

        if not image_url.lower().endswith('.png'):
            print(f'O link "{image_url}" não aponta para uma imagem PNG. Ignorando...')
            continue
        
        img_response = requests.get(image_url)
        
        if img_response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(img_response.content)
            print(f'Imagem "{filename}" baixada com sucesso!')
        else:
            print(f'Falha ao baixar a imagem "{filename}" (Código de Status: {img_response.status_code})')
    print("Todas as imagens foram baixadas com sucesso!")
else:
    print("Falha ao acessar a URL:", response.status_code)

    # Criado por Marcao - fuzzy2601
