import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# Установите максимальное количество страниц, которые вы хотите обработать
max_page_count = 1

# Запуск браузера
driver = webdriver.Chrome()  # или используйте другой драйвер в зависимости от вашего браузера

# Список для хранения ссылок
all_links = []

# Перебираем страницы
for page_number in range(1, max_page_count + 1):
    url = f"https://barnaul.medsi.ru/articles/p/{page_number}"
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    elements = driver.find_elements(By.CSS_SELECTOR, '.news-list__preview-info')
    for element in elements:
        link_element = element.find_element(By.CSS_SELECTOR, '.h2-title a')
        link_href = link_element.get_attribute('href')
        all_links.append(link_href)
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