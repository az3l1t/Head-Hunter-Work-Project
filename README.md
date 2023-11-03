# Первое задание:
Написать bash или python или groovy скрипт, который будет контролировать потребление памяти и генерировать alarm путем отправки http запроса на API.

Устанавливаем пороговое значение памяти (в процентах), при котором будет генерироваться alarm
URL API для отправки HTTP-запроса:
Некоторые из популярных веб-сервисов, которые предоставляют возможность принимать HTTP-запросы, включают:

1. RequestBin (https://requestbin.com) - сервис, который позволяет просматривать и анализировать HTTP-запросы, отправленные на его URL.

2. Beeceptor (https://beeceptor.com) - инструмент для создания виртуальной обратной связи (mock-сервера), позволяющий принимать HTTP-запросы.

3. Mockbin (https://mockbin.org) - сервис для создания HTTP-заглушек для тестирования и отладки.

# Пример использования: сайт https://beeceptor.com:
![image](https://github.com/0xolee0/first_hh/assets/126178814/b894f9cf-9f98-418c-9b84-41d132cee304)

Отправка http запроса. Код ответа 200 — один из типов кодов HTTP, информирует пользователя об успешной обработке запроса.

В бесконечном цикле инициализация потребления памяти и сопоставление с ограничением. + задержка перед следующей проверкой

# Вывод:
![image](https://github.com/0xolee0/first_hh/assets/126178814/4c569d29-81ba-4c32-94e5-32639f05b640)
