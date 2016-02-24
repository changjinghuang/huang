from selenium import webdriver  

  
driver = webdriver.Firefox()  
driver.get('http://www.python.org')  
assert 'python' in driver.title  
elem = driver.find_element_by_name('q')  
elem.send_keys('pycon')  
