import requests
import json


email = "supplier3_etp@mailforspam.com"
url = "https://api.com.mailforspam.net/"
params = {"to": email}
try:
    response = requests.get(url, params=params, timeout=10) # Проверяем статус-код HTTP, чтобы исключить ошибки сети/5xx
    response.raise_for_status()
    data = response.json()

except Exception as e:
    print(f"Ошибка соединения или парсинга: {e}")
    exit()
# success всегда true, поэтому проверяем наличие самих сообщений
if not isinstance(data, dict):
    print("Получен некорректный формат данных от API.")
    # ... (блок try-except остается прежним)
else:
    count = data.get("count", 0)

    # Проверяем правильный ключ "data", который виден в вашем выводе
    if count > 0 and "data" in data and isinstance(data["data"], list) and len(data["data"]) > 0:
        print(f"Проверка успешна. Получено {len(data['data'])} письмо(а):")
        for msg in data["data"]:
            # В некоторых случаях поле from может называться sender
            print(
                f"- Тема: {msg.get('subject', 'Без темы')}, От кого: {msg.get('from', msg.get('sender', 'Неизвестно'))}")
    else:
        print("Новых писем пока нет.")
        print("Полный ответ от API для диагностики:")
        print(json.dumps(data, indent=2, ensure_ascii=False))