import time
import psutil
import requests

# Устанавливаем пороговое значение памяти (в процентах), при котором будет генерироваться alarm
threshold = 90

# URL API для отправки HTTP-запроса
api_url = "http://your.api.url/alarm"

def generate_alarm(memory_usage):
    # Параметры для отправки HTTP-запроса
    payload = {"message": f"Memory threshold exceeded: {memory_usage}%"}
    
    # Отправка HTTP-запроса
    response = requests.post(api_url, data=payload)
    
    # Проверка статуса ответа
    if response.status_code == 200:
        print("HTTP-запрос успешно отправлен")
    else:
        print("Ошибка при отправке HTTP-запроса")

while True:
    # Получаем текущее потребление памяти в процентах
    memory_usage = psutil.virtual_memory().percent

    # Выводим информацию о потреблении памяти
    print(f"Потребление памяти: {memory_usage}%")

    # Проверяем, превышает ли потребление памяти пороговое значение
    if memory_usage > threshold:
        # Генерируем alarm через HTTP-запрос на API
        generate_alarm(memory_usage)
    
    # Задержка перед следующей проверкой
    time.sleep(10)