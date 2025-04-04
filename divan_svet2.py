# Импортируем модуль со временем
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализируем браузер
driver = webdriver.Chrome()

url = 'https://www.divan.ru/saratov/category/svet'

# Открываем веб-страницу
driver.get(url)

# Задаём 5 секунд ожидания, чтобы веб-страница успела прогрузиться
time.sleep(5)

parsed_data = []

# Парсим все товары на странице
products = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = product.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = product.find_element(By.TAG_NAME, 'a').get_attribute('href')

        parsed_data.append([name, price, url])

    except NoSuchElementException as e:
        print(f"Ошибка при парсинге: {e}")
        continue

driver.quit()

# Записываем данные в CSV
with open("ds.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название  ', 'Цена  ', 'Ссылка на товар'])
    writer.writerows(parsed_data)