from selenium import webdriver


driver = webdriver.Firefox()
driver.get('http://www.python.org')
assert 'python' in driver.title