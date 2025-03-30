from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def setup_driver():
    """Настройка Selenium WebDriver"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Фоновый режим без открытия браузера
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver


def get_paragraphs(driver):
    """Получение параграфов текущей статьи"""
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    return [p.text for p in paragraphs if p.text.strip()]


def get_links(driver):
    """Получение внутренних ссылок Википедии"""
    links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/wiki/"]:not([href*=":"])')
    return list({(link.get_attribute('href'), link.text) for link in links if link.text})[:10]


def browse_paragraphs(driver):
    """Постраничный просмотр параграфов"""
    paragraphs = get_paragraphs(driver)
    current_idx = 0

    while current_idx < len(paragraphs):
        print(f"\n=== Параграф {current_idx + 1}/{len(paragraphs)} ===")
        print(paragraphs[current_idx])

        action = input("\nДальше (Enter), назад (b), выйти (q): ").lower()
        if action == 'q':
            break
        elif action == 'b' and current_idx > 0:
            current_idx -= 1
        else:
            current_idx += 1


def select_link(driver):
    """Выбор и переход по связанной статье"""
    links = get_links(driver)
    if not links:
        print("Нет доступных связанных статей!")
        return False

    print("\nДоступные связанные статьи:")
    for i, (url, text) in enumerate(links, 1):
        print(f"{i}: {text}")

    choice = input("Выберите номер статьи (или Enter для отмены): ")
    if choice.isdigit() and 0 < int(choice) <= len(links):
        driver.get(links[int(choice) - 1][0])
        return True
    return False


def wikipedia_navigator():
    """Основная функция навигации"""
    driver = setup_driver()
    history = []

    try:
        # Начальный запрос
        search_term = input("Введите запрос для поиска в Википедии: ")
        driver.get(f"https://ru.wikipedia.org/wiki/{search_term.replace(' ', '_')}")
        history.append(driver.current_url)

        while True:
            print("\n=== Текущая статья: ===")
            print(driver.title)

            print("\nВыберите действие:")
            print("1: Листать параграфы статьи")
            print("2: Перейти на связанную страницу")
            print("3: Вернуться назад" if len(history) > 1 else "")
            print("q: Выйти")

            choice = input("Ваш выбор: ").lower()

            if choice == '1':
                browse_paragraphs(driver)
            elif choice == '2':
                if select_link(driver):
                    history.append(driver.current_url)
            elif choice == '3' and len(history) > 1:
                driver.get(history[-2])
                history.pop()
            elif choice == 'q':
                break

    finally:
        driver.quit()
        print("Программа завершена.")


if __name__ == "__main__":
    print("=== Навигатор Википедии (Selenium) ===")
    wikipedia_navigator()