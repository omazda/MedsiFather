from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from bs4 import BeautifulSoup
# Загрузка файла с ссылками
df_links = pd.read_csv('articles_links.csv')

# Создание экземпляра драйвера Chrome
driver = webdriver.Chrome()

# Список для хранения данных
data_list = []

# Перебор ссылок и парсинг
for index, row in df_links.iterrows():
    article_link = row['Article Links']

    try:
        # Открытие страницы
        driver.get(article_link)
        wait = WebDriverWait(driver, 10)
        content_div = driver.find_element(By.CLASS_NAME, 'news-detail__content')
        content_text = content_div.text
        data_list.append({
            'Number': index + 1,
            'Link': article_link,
            'Content': content_text
        })

        print(f'Title for {article_link}: {content_text}')
    except Exception as e:
        print(f'Error while parsing {article_link}: {e}')
    time.sleep(1)

# Закрытие браузера
driver.quit()

# Создание DataFrame из списка данных
df_data = pd.DataFrame(data_list)

# Запись в файл articles_data.csv
df_data.to_csv('articles_data.csv', index=False)