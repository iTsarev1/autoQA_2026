Урок 10. Allure Reports

1. Структура страницы упавшего теста
Когда ты открываешь конкретный тест в Allure (#suites/...), перед тобой несколько зон:
┌──────────────────────────────────────────────────────────────┐
│ Название теста                                              │
│ Статус: FAILED | Duration: 59s | Severity: normal           │
├──────────────────────────────────────────────────────────────┤
│ Status Message (красный блок)                                │
│   Краткая ошибка: AssertionError: Unexpected status code... │
├──────────────────────────────────────────────────────────────┤
│ Status Trace (то же поле, ниже message)                      │
│   tests/test_discount.py:61: in test_...                    │
│       ids = discount_request(data=data)                     │
│   fixtures/api/logic/quotes.py:153: in _discount_request    │
│   ...                                                       │
│   E  AssertionError: ...                                    │
├──────────────────────────────────────────────────────────────┤
│ Steps (шаги, помеченные @step — может быть пусто)            │
│ Attachments (вложения)                                       │
│   - screenshot.png                                           │
│   - log (txt — пошаговый лог всех API-запросов)              │
│   - Playwright trace (zip)                                   │
├──────────────────────────────────────────────────────────────┤
│ Parameters / Tags / Categories / Description                 │
└──────────────────────────────────────────────────────────────┘

Ключевой принцип: 
Status Message — это симптом (что пошло не так). 
Status Trace — это где пошло не так (в каком файле и на какой строке).

2. Traceback — что это и как читать
2.1. Что такое traceback
Traceback — это дорожная запись кода: путь, который проходил твой тест, от начала до момента ошибки.

3. Python генерирует его автоматически в момент падения. Формат каждой строки:
'''
файл.py:номер_строки: in имя_функции
    код_на_этой_строке
'''
3.2. Формат (на конкретном примере)
'''
tests/test_discount.py:61: in test_discount_request_draft_change
    ids = discount_request(data=data)
fixtures/api/logic/quotes.py:153: in _discount_request
    customer.quote_api.discount_request(quote_id=quote_id,
api/methods/click/quote_api.py:84: in discount_request
    return self.send_request("POST",
api/custom_requester.py:58: in send_request
    raise AssertionError(
E   AssertionError: Unexpected status code: 404, expected: 201
E   Response: {"code":404,"message":"Объект не найден.",...}
'''