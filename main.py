import os
import json
import requests

from bs4 import BeautifulSoup

# Создаем папку для сохранения изображений, если ее еще нет
os.makedirs('images', exist_ok=True)

# Счетчик для уникальных имен файлов
count = 0

import os
import json
import requests

from bs4 import BeautifulSoup

# Создаем папку для сохранения изображений, если ее еще нет
os.makedirs('images', exist_ok=True)

# Счетчик для уникальных имен файлов
count = 0

# Список для хранения данных для JSON
apps_data = []

for page_num in range(0, 100):  # страницы с 1 по 40
    url = ""
    if (count == 0):
        url = "https://happymod.com/new-mod.html"
    else:
        url = f"https://happymod.com/new-mod,{page_num}.html"
    response = requests.get(url)
    if response.status_code != 200:
        break
    soup = BeautifulSoup(response.content, 'html.parser')

    mod_images = soup.find_all(class_='pdt-list-img')

    for mod_image in mod_images:
        img_src = mod_image.find('img')['data-original']
        img_alt = mod_image.find('img')['alt']
        print("Url:", img_src)
        print("Alt:", img_alt)

        # Определяем имя файла из URL
        img_name = f"image_{count}.jpg"
        img_path = os.path.join('images', img_name)

        # Скачиваем изображение
        img_response = requests.get(img_src)
        with open(img_path, 'wb') as img_file:
            img_file.write(img_response.content)

        print(f"Изображение {img_name} скачано")

        # Создаем запись для JSON
        app_data = {
            "name": img_alt,
            "unique_id": img_name
        }
        apps_data.append(app_data)

        count += 1

# Создаем файл JSON
with open('images.json', 'w') as json_file:
    json.dump({"Apps": apps_data}, json_file, indent=4)

print("Файл images.json создан успешно.")
