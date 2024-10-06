from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
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

        # Ожидание загрузки элемента с контентом статьи
        content_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'med-articles-detail__content-wrapper'))
        )

        # Получение текста из контентного элемента до тега <span style="font-size: 10pt;">
        content_text = content_element.text.split('Источники:')[0].strip()

        # Поиск заголовка
        title_element = driver.find_element("css selector", ".med-page-banner__title__articles")
        title_text = title_element.text

        data_list.append({
            'Number': index + 1,
            'Title': title_text,
            'Link': article_link,
            'Content': content_text
        })

        print(f'Title for {article_link}: {title_text}')
        
    except Exception as e:
        print(f'Error while parsing {article_link}: {e}')
    time.sleep(1)

# Закрытие браузера
driver.quit()

# Создание DataFrame из списка данных
df_data = pd.DataFrame(data_list)

# Запись в файл articles_data.csv
df_data.to_csv('articles_data.csv', index=False)
