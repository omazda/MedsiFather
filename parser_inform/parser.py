import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Установите максимальное количество страниц, которые вы хотите обработать
max_page_count = 40

# Запуск браузера
driver = webdriver.Chrome()  # или используйте другой драйвер в зависимости от вашего браузера

# Список для хранения ссылок
all_links = []

# Перебираем страницы
for page_number in range(1, max_page_count + 1):
    url = f"https://spb.medsi.ru/articles/p/{page_number}"
    driver.get(url)
    # Проверяем, если перенаправляет на medsi.ru/articles/
    current_url = driver.current_url
    if current_url == "https://spb.medsi.ru/articles/" and page_number > 2:
        print(f"Достигнут конец страниц. Выход из цикла.")
        break
    # Парсинг ссылок
    articles = driver.find_elements(By.CLASS_NAME, "med-articles-page__article")
    links = [article.find_element(By.XPATH, ".//a[@href]").get_attribute("href") for article in articles]
    
    all_links.extend(links)

# Закрытие браузера
driver.quit()

# Сохранение в файл CSV
csv_file_path = "articles_links.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Article Links"])

    for link in all_links:
        writer.writerow([link])

print(f"Ссылки сохранены в файл: {csv_file_path}")

