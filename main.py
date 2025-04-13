import requests
from collections import defaultdict

def get_text(url):
    """Загружает текст с обработкой ошибок"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Проверка HTTP-ошибок
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка загрузки {url}: {e}")
        return None

def count_words(text, words_to_count):
    """Подсчёт слов через defaultdict (быстрее и читаемее)"""
    word_counts = defaultdict(int)
    for word in text.split():
        if word in words_to_count:
            word_counts[word] += 1
    return word_counts

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    # Чтение слов в множество для быстрого поиска
    with open(words_file, 'r') as file:
        words_to_count = {line.strip() for line in file if line.strip()}

    # Однократная загрузка текста
    text = get_text(url)
    if not text:
        return

    frequencies = count_words(text, words_to_count)
    print("Результаты подсчёта:")
    print(frequencies)

if __name__ == "__main__":
    main()