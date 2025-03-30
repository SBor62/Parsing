import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


# Функция для перевода текста на русский
def translate_to_russian(text):
    try:
        translated = GoogleTranslator(source='auto', target='ru').translate(text)
        return translated
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return text  # Возвращаем оригинальный текст в случае ошибки


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(word_definition)

        return {
            "word": russian_word,
            "definition": russian_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте ещё раз.")
            continue

        word = word_dict.get("word")
        word_definition = word_dict.get("definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user.lower() == word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()