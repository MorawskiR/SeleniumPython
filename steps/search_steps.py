from behave import given, when,then
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@given('user open helion.pl')
def step_impl(context):
    context.driver.get("https://helion.pl")

# @when('user fills "python" search input')
# def step_impl(context):
#     context.driver.find_element(By.ID,'inputSearch').send_keys('Python' + Keys.ENTER)
#     context.driver.find_element(By.ID, 'rodo-ok').click()
# #asercja spraedzanie wyniku koncowego
#
# @then('Search result = python')
# def step_imp(context):
#     context.driver.save_screenshot('zrzut3.png')
#     assert context.driver.find_element(By.CLASS_NAME, 'pytmiv--link').click()

@when('user fills "python" search input')
def step_impl(context):
    context.driver.find_element(By.ID,'inputSearch').send_keys('Python' + Keys.ENTER)


@then('Search result = python')
def step_impl(context):
    context.driver.save_screenshot('zrzut3.png')
    assert context.driver.find_element(By.CLASS_NAME, 'pytmiv--link').click()
