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
Python генерирует его автоматически в момент падения. Формат каждой строки:
'''
файл.py:номер_строки: in имя_функции
    код_на_этой_строке
'''
2.2. Формат (на конкретном примере)
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

2.3. Как читать
Два направления:
Сверху вниз | Кто кого вызвал   | Цепочка вызовов: тест → фикстура → API-метод → отправитель
Снизу вверх	| Где именно взрыв  | Последняя строка с `E` — суть ошибки

Три ключа из любого traceback:
Первая строка (`tests/test_discount.py:61`) → открываешь этот файл на эту строку — видишь, что тест делал в момент падения.
Последняя строка с `E` → сути ошибки (ожидал 201, получил 404).
Средние строки → цепочка «кто виноват»: какая фикстура, какой API-метод, какой отправитель.

2.4. Частые «ловушки» в чтении
        Симптом                          |	                Что значит
`Timeout 10000ms exceeded`	             |  Элемент не найден / не стабильный / отвалился из DOM
`element is not stable`	                 |  Элемент ещё анимируется / перемещается
`element was detached from the DOM`	     |  Элемент удалён из DOM (переотрисовка)
`No route found for METHOD URL`	         |  Бэкенд не знает METHOD+PATH (эндпоинт/метод не зарегистрированы)
`No such file or directory`	             |  Файл не существует (путь/название/окружение)
`TypeError: expected str, not NoneType`	 |  Передалась None вместо строки (данные/конфиг)
`AssertionError: check bool(False)`	     |  Soft-assert (не останавливал тест, но проверка провалилась)

2.5. Фабричные фикстуры vs обычные
Важный момент при чтении: не всякая «зелёная» фикстура в setup — это «сценарий выполнен».
Обычная фикстура (`@pytest.fixture`) — работает в setup, результат виден в `beforeStages` Allure.
Фабричная фикстура (`@pytest.fixture` + `yield function`) — в setup только создаёт функцию, реальный вызов — в теле теста: `result = factory_fixture(args)`. 
Зелёный setup ≠ «сценарий отработал».
Если в трейсбеке первая строка — это вызов фикстуры в теле теста (`ids = discount_request(data=data)`), а `beforeStages` зелёные — это фабричная фикстура. 
Падение — в теле, а не в setup.
---
