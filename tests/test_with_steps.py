import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def test_dynamic_steps():
    allure.dynamic.tag("steps")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Использование динамических шагов")
    allure.dynamic.story("Данные тесты запускаются с использованием динамических шагов")

    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        s('.search-input-container').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с имененм 'title'"):
        s(by.partial_text("title")).should(be.visible)