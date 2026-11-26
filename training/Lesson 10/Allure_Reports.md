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