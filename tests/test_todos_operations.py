from selene import browser, have


def test_complete_todo():
    browser.open('https://todomvc.com/examples/emberjs/todomvc/dist/')
    browser.element('.new-todo').type('a').press_enter()
    browser.element('.new-todo').type('b').press_enter()
    browser.element('.new-todo').type('c').press_enter()
    browser.all('.todo-list').should(have.size(1))
    # should используется для проверок чего-то. Например, be.blank - поле ввода пустое (blank) перед тем, как вводить текст.
    # should.visible - проверяет, что элемент видимый на странице
    # should.not.visible - проверяет, что элемент НЕ видимый на странице
    # should(have.size(1)) - Проверяет, что количество элементов в коллекции равно 1