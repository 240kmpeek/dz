import openai
import pyttsx3
import speech_recognition as sr

# Настройка API-ключа для GPT-3.5
openai.api_key = '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'

# Инициализация движка синтеза речи
engine = pyttsx3.init()

# Словарь для кэширования ответов
response_cache = {}

# Функция для распознавания речи пользователя
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", text)
        return text
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
        return ""
    except sr.RequestError:
        print("Не удалось подключиться к сервису распознавания")
        return ""

# Функция для взаимодействия с GPT-3.5 и кеширования ответов
def interact_with_gpt3(prompt):
    # Проверяем, есть ли ответ в кэше
    if prompt in response_cache:
        return response_cache[prompt]

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )

    # Сохраняем ответ в кэше
    response_text = response.choices[0].text
    response_cache[prompt] = response_text

    return response_text

# Функция для синтеза речи и воспроизведения ответа
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Основной цикл работы ассистента
while True:
    print("Говорите или нажмите Ctrl+C для выхода.")
    user_input = recognize_speech()

    if user_input:
        response = interact_with_gpt3(user_input)
        print("Ответ:", response)
        speak(response)